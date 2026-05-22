from __future__ import annotations

from collections import Counter
from pathlib import Path


def parse_retrans_stream(path: str | Path) -> list[dict[str, int | str]]:
    events: list[dict[str, int | str]] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        timestamp_ns, comm, src_port = line.split()
        events.append(
            {
                "timestamp_ns": int(timestamp_ns),
                "comm": comm,
                "src_port": int(src_port),
            }
        )
    return events


def summarize_retrans_stream(path: str | Path) -> dict[str, object]:
    events = parse_retrans_stream(path)
    by_process = Counter(event["comm"] for event in events)
    by_port = Counter(event["src_port"] for event in events)

    top_processes = [
        {"comm": comm, "retransmissions": count}
        for comm, count in by_process.most_common(5)
    ]
    top_ports = [
        {"src_port": port, "retransmissions": count}
        for port, count in by_port.most_common(5)
    ]

    return {
        "events": len(events),
        "top_processes": top_processes,
        "top_ports": top_ports,
    }

