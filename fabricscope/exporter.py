from __future__ import annotations

from pathlib import Path

from fabricscope.analyzer import build_report


def export_prometheus(input_path: str, output_path: str) -> str:
    report = build_report(input_path)
    lines = [
        "# HELP fabricscope_events_total Number of ingested events.",
        "# TYPE fabricscope_events_total gauge",
        f"fabricscope_events_total {report['events']}",
        "# HELP fabricscope_congestion_epochs_total Count of detected congestion epochs.",
        "# TYPE fabricscope_congestion_epochs_total gauge",
        f"fabricscope_congestion_epochs_total {len(report['congestion_epochs'])}",
    ]

    for hotspot in report["top_hotspots"]:
        edge = f'src="{hotspot["src"]}",dst="{hotspot["dst"]}"'
        lines.append(
            f"fabricscope_hotspot_score{{{edge}}} {hotspot['congestion_score']}"
        )
        lines.append(
            f"fabricscope_hotspot_retransmissions{{{edge}}} {hotspot['retransmissions']}"
        )

    output = "\n".join(lines) + "\n"
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding="utf-8")
    return output

