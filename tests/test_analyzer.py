from fabricscope.analyzer import build_report, load_events, rank_hotspots


def test_hotspots_rank_checkpoint_sync_first() -> None:
    events = load_events("data/sample_fabric_events.csv")
    hotspots = rank_hotspots(events)
    assert hotspots[0].dst == "leaf-02"
    assert hotspots[0].retransmissions >= hotspots[1].retransmissions


def test_report_detects_pause_epochs() -> None:
    report = build_report("data/sample_fabric_events.csv")
    assert report["events"] == 10
    assert len(report["congestion_epochs"]) >= 4
