from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

from fabricscope.models import FabricEvent


@dataclass(frozen=True, slots=True)
class Hotspot:
    src: str
    dst: str
    congestion_score: float
    retransmissions: int
    ecn_marks: int
    max_queue_depth_kb: int
    total_pause_us: int


@dataclass(frozen=True, slots=True)
class FlowPressure:
    flow: str
    packets: int
    retransmissions: int
    ecn_marks: int
    avg_latency_us: float


def load_events(path: str | Path) -> list[FabricEvent]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            FabricEvent(
                timestamp_ms=int(row["timestamp_ms"]),
                src=row["src"],
                dst=row["dst"],
                flow=row["flow"],
                protocol=row["protocol"],
                latency_us=int(row["latency_us"]),
                retransmissions=int(row["retransmissions"]),
                ecn_marks=int(row["ecn_marks"]),
                queue_depth_kb=int(row["queue_depth_kb"]),
                pfc_pause_us=int(row["pfc_pause_us"]),
            )
            for row in reader
        ]


def rank_hotspots(events: list[FabricEvent]) -> list[Hotspot]:
    buckets: dict[tuple[str, str], list[FabricEvent]] = defaultdict(list)
    for event in events:
        buckets[event.edge].append(event)

    hotspots: list[Hotspot] = []
    for edge, group in buckets.items():
        retransmissions = sum(item.retransmissions for item in group)
        ecn_marks = sum(item.ecn_marks for item in group)
        max_queue = max(item.queue_depth_kb for item in group)
        total_pause = sum(item.pfc_pause_us for item in group)
        avg_latency = sum(item.latency_us for item in group) / len(group)
        congestion_score = (
            retransmissions * 3.0
            + ecn_marks * 1.2
            + max_queue / 8.0
            + total_pause / 100.0
            + avg_latency / 50.0
        )
        hotspots.append(
            Hotspot(
                src=edge[0],
                dst=edge[1],
                congestion_score=round(congestion_score, 2),
                retransmissions=retransmissions,
                ecn_marks=ecn_marks,
                max_queue_depth_kb=max_queue,
                total_pause_us=total_pause,
            )
        )

    return sorted(hotspots, key=lambda item: item.congestion_score, reverse=True)


def rank_flow_pressure(events: list[FabricEvent]) -> list[FlowPressure]:
    buckets: dict[str, list[FabricEvent]] = defaultdict(list)
    for event in events:
        buckets[event.flow].append(event)

    rankings: list[FlowPressure] = []
    for flow, group in buckets.items():
        rankings.append(
            FlowPressure(
                flow=flow,
                packets=len(group),
                retransmissions=sum(item.retransmissions for item in group),
                ecn_marks=sum(item.ecn_marks for item in group),
                avg_latency_us=round(
                    sum(item.latency_us for item in group) / len(group), 2
                ),
            )
        )
    return sorted(
        rankings,
        key=lambda item: (item.retransmissions, item.ecn_marks, item.avg_latency_us),
        reverse=True,
    )


def detect_congestion_epochs(
    events: list[FabricEvent], queue_threshold_kb: int = 128
) -> list[dict[str, int | str]]:
    epochs: list[dict[str, int | str]] = []
    for event in events:
        if event.queue_depth_kb >= queue_threshold_kb or event.pfc_pause_us > 0:
            epochs.append(
                {
                    "timestamp_ms": event.timestamp_ms,
                    "src": event.src,
                    "dst": event.dst,
                    "flow": event.flow,
                    "queue_depth_kb": event.queue_depth_kb,
                    "pfc_pause_us": event.pfc_pause_us,
                }
            )
    return epochs


def build_report(path: str | Path) -> dict[str, object]:
    events = load_events(path)
    return {
        "events": len(events),
        "top_hotspots": [asdict(item) for item in rank_hotspots(events)[:5]],
        "top_flows": [asdict(item) for item in rank_flow_pressure(events)[:5]],
        "congestion_epochs": detect_congestion_epochs(events),
    }

