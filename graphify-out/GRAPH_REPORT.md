# Graph Report - .  (2026-05-22)

## Corpus Check
- 8 files · ~1,791 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 24 nodes · 34 edges · 5 communities detected
- Extraction: 65% EXTRACTED · 35% INFERRED · 0% AMBIGUOUS · INFERRED: 12 edges (avg confidence: 0.75)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]

## God Nodes (most connected - your core abstractions)
1. `build_report()` - 8 edges
2. `FabricEvent` - 4 edges
3. `export_prometheus()` - 4 edges
4. `load_events()` - 4 edges
5. `rank_hotspots()` - 4 edges
6. `main()` - 4 edges
7. `test_hotspots_rank_checkpoint_sync_first()` - 3 edges
8. `compare_runtime()` - 3 edges
9. `Hotspot` - 3 edges
10. `FlowPressure` - 3 edges

## Surprising Connections (you probably didn't know these)
- `test_report_detects_pause_epochs()` --calls--> `build_report()`  [INFERRED]
  tests/test_analyzer.py → fabricscope/analyzer.py
- `test_hotspots_rank_checkpoint_sync_first()` --calls--> `rank_hotspots()`  [INFERRED]
  tests/test_analyzer.py → fabricscope/analyzer.py
- `test_hotspots_rank_checkpoint_sync_first()` --calls--> `load_events()`  [INFERRED]
  tests/test_analyzer.py → fabricscope/analyzer.py
- `test_export_prometheus_writes_metrics_file()` --calls--> `export_prometheus()`  [INFERRED]
  tests/test_exporter.py → fabricscope/exporter.py
- `test_compare_runtime_reports_kernel_share()` --calls--> `compare_runtime()`  [INFERRED]
  tests/test_exporter.py → fabricscope/runtime_compare.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.25
Nodes (5): main(), export_prometheus(), compare_runtime(), test_compare_runtime_reports_kernel_share(), test_export_prometheus_writes_metrics_file()

### Community 1 - "Community 1"
Cohesion: 0.52
Nodes (6): build_report(), detect_congestion_epochs(), FlowPressure, Hotspot, rank_flow_pressure(), rank_hotspots()

### Community 2 - "Community 2"
Cohesion: 0.5
Nodes (3): load_events(), test_hotspots_rank_checkpoint_sync_first(), test_report_detects_pause_epochs()

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (1): FabricEvent

### Community 4 - "Community 4"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **Thin community `Community 4`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_report()` connect `Community 1` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.531) - this node is a cross-community bridge._
- **Why does `main()` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.273) - this node is a cross-community bridge._
- **Why does `export_prometheus()` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.209) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `build_report()` (e.g. with `test_report_detects_pause_epochs()` and `export_prometheus()`) actually correct?**
  _`build_report()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `FabricEvent` (e.g. with `Hotspot` and `FlowPressure`) actually correct?**
  _`FabricEvent` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `export_prometheus()` (e.g. with `test_export_prometheus_writes_metrics_file()` and `build_report()`) actually correct?**
  _`export_prometheus()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `load_events()` (e.g. with `test_hotspots_rank_checkpoint_sync_first()` and `FabricEvent`) actually correct?**
  _`load_events()` has 2 INFERRED edges - model-reasoned connections that need verification._