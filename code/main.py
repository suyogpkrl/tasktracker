import tasks
import storage


def main():
    while True:
        print("\n--- Task Tracker ---\n"
            "1. Add Task\n"
            "2. List Tasks\n"
            "3. Mark Task as Done\n"
            "4. Remove Task\n"
            "5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            tasks.add_task(task)
        elif choice == "2":
            mode_choice = input(
                "Select task type to list:\n"
                "1. All tasks\n"
                "2. Pending tasks\n"
                "3. Completed tasks\n"
                "Enter choice (1-3): "
            )
            if mode_choice == "1":
                tasks.list_tasks("all")
            if mode_choice == "2":
                tasks.list_tasks("pending")
            if mode_choice == "3":
                task.list_tasks("done")

        elif choice == "3":
            index = int(input("Enter task number to mark done: "))
            tasks.mark_done(index)

        elif choice == "4":
            index = int(input("Enter task number to remove: "))
            tasks.remove_task(index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()