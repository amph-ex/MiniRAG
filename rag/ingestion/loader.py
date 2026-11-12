from pathlib import Path
BASE=Path(__file__).resolve().parents[2]
def get_content():
    path= BASE / "source" / "source.txt"
    return path.read_text(encoding="utf-8")