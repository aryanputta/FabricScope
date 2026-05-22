# Project Brief

Project: FabricScope
Gap: Existing fabric telemetry stacks expose counters, but fail to localize which node pair or flow is causing congestion collapse under bursty collective traffic.
Stack: Python 3.11+, CSV event ingestion, simple CLI, deterministic benchmark data, optional bpftrace probes
Data: `data/sample_fabric_events.csv`

Build:
1. Event ingestion: parse flow telemetry into typed records and validate schema.
2. Hotspot ranking: aggregate by edge, score congestion, and rank hotspots.
3. Flow pressure analysis: rank flows by retransmission, ECN pressure, and latency.
4. Congestion epoch detection: surface queue spikes and pause storms.
5. Benchmark surface: deterministic sample data, repeatable JSON report, probe examples.

Benchmark against: manual dashboard-style triage without hotspot ranking
Success: report surfaces the heaviest congestion edge and flags pause-heavy epochs deterministically on the sample dataset

