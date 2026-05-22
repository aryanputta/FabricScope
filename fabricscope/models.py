from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FabricEvent:
    timestamp_ms: int
    src: str
    dst: str
    flow: str
    protocol: str
    latency_us: int
    retransmissions: int
    ecn_marks: int
    queue_depth_kb: int
    pfc_pause_us: int

    @property
    def edge(self) -> tuple[str, str]:
        return (self.src, self.dst)

