from __future__ import annotations

import csv
from pathlib import Path


def compare_runtime(path: str) -> dict[str, object]:
    rows = list(csv.DictReader(Path(path).open(encoding="utf-8")))
    kernel_total = sum(int(row["kernel_us"]) for row in rows)
    runtime_total = sum(int(row["runtime_us"]) for row in rows)
    packets = len(rows)
    return {
        "packets": packets,
        "avg_kernel_us": round(kernel_total / packets, 2),
        "avg_runtime_us": round(runtime_total / packets, 2),
        "kernel_share_pct": round((kernel_total / max(kernel_total + runtime_total, 1)) * 100.0, 2),
    }

