from pathlib import Path

from fabricscope.exporter import export_prometheus
from fabricscope.runtime_compare import compare_runtime


def test_export_prometheus_writes_metrics_file(tmp_path: Path) -> None:
    output_path = tmp_path / "metrics.prom"
    payload = export_prometheus("data/sample_fabric_events.csv", str(output_path))
    assert "fabricscope_events_total 10" in payload
    assert output_path.exists()


def test_compare_runtime_reports_kernel_share() -> None:
    payload = compare_runtime("data/sample_runtime_trace.csv")
    assert payload["packets"] == 5
    assert payload["kernel_share_pct"] > 50
