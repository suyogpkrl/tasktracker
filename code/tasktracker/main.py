# Main entry point for the Task Tracker CLI application

import tasks
import argparse

# Initialize argument parser for the CLI
parser = argparse.ArgumentParser(prog="tracker",description="Simple Task Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

# Subcommand: add a new task
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("task_desc", type = str, help = "Task description")

# Subcommand: list tasks with optional filter
list_parser = subparsers.add_parser("list", help = "List all tasks")
list_parser.add_argument(
    "filter",
    nargs = "?",
    default = "all",
    choices = ["all", "pending", "done"],
    help = "Filter tasks: all, pending, or done."
)

# Subcommand: remove a task by ID
remove_parser = subparsers.add_parser("remove", help = "Remove a task")
remove_parser.add_argument("task_id", type = int, help = "Task index")

# Subcommand: mark a task as completed
done_parser = subparsers.add_parser("done", help = "Mark task as done")
done_parser.add_argument("task_id", type = int, help = "Id of done task")


def main():
    """Parse command line arguments and route to appropriate task function."""
    args = parser.parse_args()

    # Route commands to their respective handlers
    if args.command == "add":
        tasks.add_task(args.task_desc)
    elif args.command == "list":
        # List tasks with the specified filter
        if args.filter == "pending":
            tasks.list_tasks("pending")
        elif args.filter == "done":
            tasks.list_tasks("done")
        else:
            tasks.list_tasks("all")

    elif args.command == "done":
        tasks.mark_done(args.task_id)

    elif args.command == "remove":
        tasks.remove_task(args.task_id)

    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()