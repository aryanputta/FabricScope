# Graph Report - .  (2026-05-22)

## Corpus Check
- 9 files · ~2,318 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 30 nodes · 45 edges · 7 communities detected
- Extraction: 62% EXTRACTED · 38% INFERRED · 0% AMBIGUOUS · INFERRED: 17 edges (avg confidence: 0.76)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]

## God Nodes (most connected - your core abstractions)
1. `build_report()` - 9 edges
2. `main()` - 6 edges
3. `FabricEvent` - 4 edges
4. `export_prometheus()` - 4 edges
5. `export_signalmesh_bundle()` - 4 edges
6. `load_events()` - 4 edges
7. `rank_hotspots()` - 4 edges
8. `summarize_retrans_stream()` - 4 edges
9. `test_hotspots_rank_checkpoint_sync_first()` - 3 edges
10. `compare_runtime()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `test_report_detects_pause_epochs()` --calls--> `build_report()`  [INFERRED]
  tests/test_analyzer.py → fabricscope/analyzer.py
- `test_hotspots_rank_checkpoint_sync_first()` --calls--> `rank_hotspots()`  [INFERRED]
  tests/test_analyzer.py → fabricscope/analyzer.py
- `test_export_prometheus_writes_metrics_file()` --calls--> `export_prometheus()`  [INFERRED]
  tests/test_exporter.py → fabricscope/exporter.py
- `test_summarize_retrans_stream_reports_top_process()` --calls--> `summarize_retrans_stream()`  [INFERRED]
  tests/test_exporter.py → fabricscope/live_capture.py
- `test_hotspots_rank_checkpoint_sync_first()` --calls--> `load_events()`  [INFERRED]
  tests/test_analyzer.py → fabricscope/analyzer.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (4): load_events(), FabricEvent, test_hotspots_rank_checkpoint_sync_first(), test_report_detects_pause_epochs()

### Community 1 - "Community 1"
Cohesion: 0.52
Nodes (6): build_report(), detect_congestion_epochs(), FlowPressure, Hotspot, rank_flow_pressure(), rank_hotspots()

### Community 2 - "Community 2"
Cohesion: 0.4
Nodes (4): main(), export_prometheus(), export_signalmesh_bundle(), test_export_signalmesh_bundle_writes_bundle_and_report()

### Community 3 - "Community 3"
Cohesion: 0.67
Nodes (2): compare_runtime(), test_compare_runtime_reports_kernel_share()

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (2): test_export_prometheus_writes_metrics_file(), test_summarize_retrans_stream_reports_top_process()

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (2): parse_retrans_stream(), summarize_retrans_stream()

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **Thin community `Community 6`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_report()` connect `Community 1` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.525) - this node is a cross-community bridge._
- **Why does `main()` connect `Community 2` to `Community 1`, `Community 3`, `Community 5`?**
  _High betweenness centrality (0.388) - this node is a cross-community bridge._
- **Why does `summarize_retrans_stream()` connect `Community 5` to `Community 2`, `Community 4`?**
  _High betweenness centrality (0.175) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `build_report()` (e.g. with `test_report_detects_pause_epochs()` and `export_prometheus()`) actually correct?**
  _`build_report()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `main()` (e.g. with `export_prometheus()` and `export_signalmesh_bundle()`) actually correct?**
  _`main()` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `FabricEvent` (e.g. with `Hotspot` and `FlowPressure`) actually correct?**
  _`FabricEvent` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `export_prometheus()` (e.g. with `test_export_prometheus_writes_metrics_file()` and `build_report()`) actually correct?**
  _`export_prometheus()` has 3 INFERRED edges - model-reasoned connections that need verification._