from storage import load_tasks, save_tasks


def add_task(task: str) -> None:
    tasks = load_tasks()
    tasks.append({"description": task, "done": False})
    save_tasks(tasks)


def remove_task(index: int) -> None:
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed: {removed['description']}") 
    else:
        print("Invalid task number")

def list_tasks(mode: str = 'all') -> None:
    tasks = load_tasks()

    if mode == "pending":
        tasks_to_show = [t for t in tasks if t["done"]==False]
    elif mode == "done":
        tasks_to_show = [t for t in tasks if t["done"]==True]
    else:
        tasks_to_show = tasks

    if not tasks_to_show:
        print("No tasks to show.")
        return

    for i, task in enumerate(tasks_to_show, start = 1):
        status = "[✓]" if task["done"] == True else "[ ]"
        print(f"{i}. {status} {task['description']}")

def mark_done(index: int) -> None:
    tasks = load_tasks()

    if 0<= index - 1 < len(tasks):
        task = tasks[index - 1]

        if not task["done"]:
            task["done"] = True
            save_tasks(tasks)
            print(f"Marked as done: {task['description']}")
        else:
            print("Task is already completed.")
    else:
        print("Invalid task number.")