import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok = True)

TASKS_FILE = DATA_DIR / "tasks.json"

def load_tasks() -> list[dict]:
    if not TASKS_FILE.exists():
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks: list[dict]) -> None:
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent = 4)
