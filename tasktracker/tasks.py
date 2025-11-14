# Task management functions for adding, removing, listing, and updating tasks

from tasktracker import storage


def add_task(task: str) -> None:
    """Add a new task to the task list."""
    tasks = storage.load_tasks()
    tasks.append({"description": task, "done": False})
    storage.save_tasks(tasks)
    print("Task added successfully")


def remove_task(index: int) -> None:
    """Remove a task by its index (1-based indexing)."""
    tasks = storage.load_tasks()
    # Convert 1-based index to 0-based for list access
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        storage.save_tasks(tasks)
        print(f"Removed: {removed['description']}") 
    else:
        print("Invalid task number")

def list_tasks(mode: str = 'all') -> None:
    """Display tasks filtered by status (all, pending, or done)."""
    tasks = storage.load_tasks()

    # Filter tasks based on completion status
    if mode == "pending":
        tasks_to_show = [t for t in tasks if t["done"]==False]
    elif mode == "done":
        tasks_to_show = [t for t in tasks if t["done"]==True]
    else:
        tasks_to_show = tasks

    if not tasks_to_show:
        print("No tasks to show.")
        return

    # Display tasks with checkmark or empty box and 1-based numbering
    for i, task in enumerate(tasks_to_show, start = 1):
        status = "[✓]" if task["done"] == True else "[ ]"
        print(f"{i}. {status} {task['description']}")

def mark_done(index: int) -> None:
    """Mark a task as completed by its index (1-based indexing)."""
    tasks = storage.load_tasks()

    # Convert 1-based index to 0-based for list access
    if 0<= index - 1 < len(tasks):
        task = tasks[index - 1]

        # Only update if task is not already completed
        if not task["done"]:
            task["done"] = True
            storage.save_tasks(tasks)
            print(f"Marked as done: {task['description']}")
        else:
            print("Task is already completed.")
    else:
        print("Invalid task number.")