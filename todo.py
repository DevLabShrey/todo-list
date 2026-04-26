

import datetime


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            tasks = []
            for line in lines:
                tasks.append(line.strip())
            return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter task: ")

    print("Priority levels: High / Medium / Low")
    priority = input("Enter priority: ").capitalize()

    if priority not in ["High", "Medium", "Low"]:
        priority = "Low"

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    formatted_task = f"[{priority}] {task} (Added: {time})"

    tasks.append(formatted_task)
    save_tasks(tasks)

    print("Task added successfully!")



def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n----- YOUR TASKS -----")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_complete(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to mark complete: ")) - 1

        if 0 <= index < len(tasks):
            if "[✓]" not in tasks[index]:
                tasks[index] = "[✓] " + tasks[index]
                save_tasks(tasks)
                print("Marked as complete!")
            else:
                print("Already completed.")
        else:
            print("Invalid number.")

    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")

    except ValueError:
        print("Enter a valid number.")



def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
