import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def read_json(file_name: str) -> dict:
    file_path = PROJECT_ROOT / "test_data" / file_name

    with file_path.open(mode="r", encoding="utf-8") as file:
        return json.load(file)