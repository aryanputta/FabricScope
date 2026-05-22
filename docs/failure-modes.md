# Failure Modes

- Sparse telemetry can understate real congestion if the collector drops events.
- Counter-only data cannot prove causality without time correlation to step time.
- Probe overhead can bias measurements in real deployments. The sample repo keeps this as a future benchmark surface instead of claiming it away.
- RoCE-specific pathologies such as PFC deadlock require richer signals than the sample CSV currently provides.

