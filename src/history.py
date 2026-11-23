import json
from pathlib import Path
from datetime import datetime

HISTORY_FILE = Path("analysis_history.json")

def load_history():
    if not HISTORY_FILE.exists():
        return []
    try:
        return json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

def add_record(filename, width, height, brightness, contrast):
    records = load_history()
    records.insert(0, {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "filename": filename,
        "width_px": width,
        "height_px": height,
        "brightness": brightness,
        "contrast": contrast
    })
    HISTORY_FILE.write_text(json.dumps(records[:100], indent=2), encoding="utf-8")

def clear_history():
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
