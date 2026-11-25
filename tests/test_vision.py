import numpy as np
from PIL import Image

from src import history
from src.vision import analyse_image, demo_classify


def test_analyse_image_reports_size_and_statistics():
    img = Image.fromarray(np.full((20, 30, 3), 128, dtype=np.uint8))
    r = analyse_image(img)
    assert (r["width"], r["height"]) == (30, 20)
    assert abs(r["brightness"] - 128 / 255) < 1e-3
    assert r["contrast"] == 0.0


def test_demo_classify_rules():
    assert demo_classify(0.1, 0.2)[0] == "Low-light image"
    assert demo_classify(0.5, 0.7)[0] == "High-contrast image"
    label, score, _ = demo_classify(0.5, 0.2)
    assert label == "Balanced image" and 0 < score <= 0.95


def test_history_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(history, "HISTORY_FILE", tmp_path / "h.json")
    assert history.load_history() == []
    history.add_record("a.jpg", 10, 20, 0.5, 0.1)
    assert history.load_history()[0]["filename"] == "a.jpg"
    history.clear_history()
    assert history.load_history() == []
