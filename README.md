# Task Tracker

A lightweight command-line task management tool to help you organize and track your daily tasks efficiently.

## Features

- ✅ Add new tasks
- 📋 List all tasks or filter by status (pending/done)
- ✔️ Mark tasks as completed
- 🗑️ Remove tasks
- 💾 Persistent storage using JSON

## Installation

Clone the repository and install in development mode:

```bash
git clone <your-repo-url>
cd task-tracker
pip install -e .
```

Or install with development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

Once installed, use the `tracker` command from anywhere:

### Add a task
```bash
tracker add "Buy groceries"
tracker add "Complete project report"
```

### List tasks
```bash
tracker list              # Show all tasks
tracker list pending      # Show only pending tasks
tracker list done         # Show only completed tasks
```

### Mark a task as done
```bash
tracker done 1    # Mark task 1 as completed
```

### Remove a task
```bash
tracker remove 2   # Delete task 2
```

### Get help
```bash
tracker --help
tracker list --help
```

## Project Structure

```
task-tracker/
├── tasktracker/
│   ├── __init__.py
│   ├── cli.py           # CLI entry point and argument parsing
│   ├── tasks.py         # Task management logic
│   ├── storage.py       # Task persistence (JSON)
│   └── data/
│       └── tasks.json   # Task storage file (auto-created)
├── pyproject.toml       # Project configuration & dependencies
├── .gitignore
└── README.md
```

## Development

Install dev dependencies:
```bash
pip install -e ".[dev]"
```

Run tests:
```bash
pytest
```

Format code:
```bash
black tasktracker/
isort tasktracker/
```

Type check:
```bash
mypy tasktracker/
```

## License

MIT License - see LICENSE file for details.

## Author

Suyog Pokhrel (pokhrels477@gmail.com)
