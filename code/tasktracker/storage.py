# Storage module for managing task persistence using JSON files

import json
from pathlib import Path

# Set base directory to the current module's location
BASE_DIR = Path(__file__).parent

# Create data directory for storing task files
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok = True)

# Path to the JSON file storing all tasks
TASKS_FILE = DATA_DIR / "tasks.json"

def load_tasks() -> list[dict]:
    """Load tasks from JSON file. Returns empty list if file doesn't exist or is invalid."""
    if not TASKS_FILE.exists():
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Handle corrupted JSON file by returning empty list
        return []

def save_tasks(tasks: list[dict]) -> None:
    """Save tasks to JSON file with pretty formatting."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent = 4)
