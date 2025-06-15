import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILENAME = BASE_DIR / "menu.json"


def ensure_data_file():
    if not FILENAME.exists():
        from app.scraper import main
        main()


def load_products(filename=FILENAME):
    ensure_data_file()
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_products(data, filename=FILENAME):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
