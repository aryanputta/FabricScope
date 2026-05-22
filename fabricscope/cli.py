from __future__ import annotations

import argparse
import json

from fabricscope.analyzer import build_report
from fabricscope.exporter import export_prometheus
from fabricscope.live_capture import summarize_retrans_stream
from fabricscope.runtime_compare import compare_runtime


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze ML fabric event logs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    report = subparsers.add_parser("report", help="Build a congestion report.")
    report.add_argument("--input", required=True, help="Path to CSV event log.")
    report.add_argument(
        "--format",
        choices=("json", "pretty"),
        default="pretty",
        help="Output format.",
    )

    export_cmd = subparsers.add_parser(
        "export-prometheus", help="Export hotspot metrics in Prometheus text format."
    )
    export_cmd.add_argument("--input", required=True, help="Path to CSV event log.")
    export_cmd.add_argument("--output", required=True, help="Output metrics file.")

    compare_cmd = subparsers.add_parser(
        "compare-runtime",
        help="Compare time spent in the Linux kernel versus runtime processing.",
    )
    compare_cmd.add_argument("--input", required=True, help="Path to runtime trace CSV.")
    compare_cmd.add_argument(
        "--format",
        choices=("json", "pretty"),
        default="pretty",
        help="Output format.",
    )

    live_cmd = subparsers.add_parser(
        "summarize-retrans",
        help="Summarize a bpftrace-style retransmission stream.",
    )
    live_cmd.add_argument("--input", required=True, help="Path to retransmission text log.")
    live_cmd.add_argument(
        "--format",
        choices=("json", "pretty"),
        default="pretty",
        help="Output format.",
    )

    args = parser.parse_args()
    if args.command == "export-prometheus":
        print(export_prometheus(args.input, args.output), end="")
        return
    if args.command == "compare-runtime":
        payload = compare_runtime(args.input)
        if args.format == "json":
            print(json.dumps(payload, indent=2, sort_keys=True))
            return
        print(
            f"packets={payload['packets']} avg_kernel_us={payload['avg_kernel_us']} "
            f"avg_runtime_us={payload['avg_runtime_us']} kernel_share_pct={payload['kernel_share_pct']}"
        )
        return
    if args.command == "summarize-retrans":
        payload = summarize_retrans_stream(args.input)
        if args.format == "json":
            print(json.dumps(payload, indent=2, sort_keys=True))
            return
        print(f"events={payload['events']}")
        print("top_processes:")
        for item in payload["top_processes"]:
            print(f"  {item['comm']} retrans={item['retransmissions']}")
        print("top_ports:")
        for item in payload["top_ports"]:
            print(f"  {item['src_port']} retrans={item['retransmissions']}")
        return

    payload = build_report(args.input)

    if args.format == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
        return

    print(f"events={payload['events']}")
    print("top_hotspots:")
    for item in payload["top_hotspots"]:
        print(
            f"  {item['src']}->{item['dst']} score={item['congestion_score']} "
            f"retrans={item['retransmissions']} ecn={item['ecn_marks']} "
            f"queue_kb={item['max_queue_depth_kb']}"
        )
    print("top_flows:")
    for item in payload["top_flows"]:
        print(
            f"  {item['flow']} packets={item['packets']} retrans={item['retransmissions']} "
            f"ecn={item['ecn_marks']} avg_latency_us={item['avg_latency_us']}"
        )
    print(f"congestion_epochs={len(payload['congestion_epochs'])}")


if __name__ == "__main__":
    main()
