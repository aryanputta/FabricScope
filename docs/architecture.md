# Architecture

FabricScope uses a narrow pipeline:

1. `load_events()` parses structured telemetry.
2. `rank_hotspots()` groups by source-destination edge and computes a congestion score.
3. `rank_flow_pressure()` identifies top talkers and retransmission-heavy flows.
4. `detect_congestion_epochs()` isolates queue spikes and pause-heavy windows.
5. `fabricscope report` emits a deterministic summary for repeatable benchmarking.

This repo intentionally stops at observability. It does not perform routing, scheduling, or congestion control decisions.

