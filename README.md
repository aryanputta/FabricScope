# FabricScope

FabricScope is a production-style observability toolkit for ML infrastructure fabrics. It ingests flow-level event logs that resemble what an eBPF or NIC telemetry pipeline would emit, then ranks congestion hotspots, loss domains, and noisy flows.

## Gap

Modern GPU fabrics expose huge amounts of counters, but infra teams still struggle to connect raw retransmissions, ECN marks, pause storms, and handshake latency to the actual bottlenecking flow or node pair. Existing dashboards often stop at counter visualization instead of failure attribution.

Gap statement:

> Existing fabric telemetry stacks expose counters, but fail to localize which node pair, flow class, or congestion epoch actually causes transport collapse under bursty collective traffic.

## Target Alignment

- xAI: Ethernet and RoCE debugging for large-scale training fabrics
- NVIDIA: observability and performance triage around NIC, DPU, and collective traffic
- Apple: low-level network observability and anomaly localization

## Repo Layout

```text
fabricscope/
├── analyzer.py
├── cli.py
├── exporter.py
└── models.py
data/
└── sample_fabric_events.csv
dashboards/
└── fabricscope_grafana.json
probes/
├── tcp_retrans.bt
└── rdma_latency.bt
tests/
└── test_analyzer.py
```

## Quickstart

```bash
make setup
make report
make test
```

## Example

```bash
.venv/bin/fabricscope report --input data/sample_fabric_events.csv --format json
.venv/bin/fabricscope export-prometheus --input data/sample_fabric_events.csv --output results/metrics.prom
.venv/bin/fabricscope compare-runtime --input data/sample_runtime_trace.csv --format json
.venv/bin/fabricscope summarize-retrans --input data/sample_tcp_retrans.log --format json
```

## Benchmark Target

- Export TCP retransmission and hotspot metrics into Prometheus text format
- Provide a starter Grafana dashboard
- Compare kernel time versus runtime time for a Helios-style runtime trace
- Summarize a live `tcp_retransmit_skb` capture into process and port hotspots

## Success Metrics

- Surfaces top hotspot nodes by congestion score
- Ranks top talkers by retransmission and ECN pressure
- Detects queue pressure epochs in deterministic input data
