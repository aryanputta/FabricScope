# Live Runbook

## Goal

Capture live TCP retransmissions with `bpftrace`, summarize the stream, and export evidence that identifies which process and port are generating retransmission pressure.

## Prerequisites

- Linux host with `bpftrace`
- sudo privileges
- kernel support for the `tcp:tcp_retransmit_skb` tracepoint

## Capture

```bash
bash scripts/run_bpftrace_live.sh results/live_tcp_retrans.log
```

## Summarize

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
python -m fabricscope.cli summarize-retrans --input results/live_tcp_retrans.log --format json
```

## What To Save

- total retransmission events
- top offending processes
- top offending source ports
- timestamp of capture
- concurrent runtime or workload running during the capture

## Credible Benchmark

Run a workload that intentionally causes queue pressure, capture retransmissions before and after a change, and show:

- reduced retransmission count
- reduced hotspot concentration
- explanation of what changed
