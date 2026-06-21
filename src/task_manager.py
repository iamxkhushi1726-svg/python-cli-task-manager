import json
import argparse
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Return empty list if file doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save the tasks list to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(title, priority="medium"):
    """Add a new task with a title, priority, and timestamp."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + f"[ADDED] Task #{task['id']}: {title} ({priority} priority)")


def list_tasks(show_all=False):
    """Display all tasks or only pending ones."""
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "No tasks yet. Add one with: python src/task_manager.py add 'Your task'")
        return

    print(Fore.CYAN + "\n--- Your Tasks ---")
    for task in tasks:
        if not show_all and task["done"]:
            continue
        status = Fore.GREEN + "[DONE]" if task["done"] else Fore.RED + "[TODO]"
        priority_color = {
            "high": Fore.RED,
            "medium": Fore.YELLOW,
            "low": Fore.GREEN
        }.get(task["priority"], Fore.WHITE)

        print(
            f"{status} #{task['id']} "
            f"{Style.BRIGHT}{task['title']}{Style.RESET_ALL} "
            f"| {priority_color}{task['priority'].upper()}{Style.RESET_ALL} "
            f"| {task['created_at']}"
        )
    print()


def complete_task(task_id):
    """Mark a task as completed by its ID."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(Fore.GREEN + f"[COMPLETED] Task #{task_id}: {task['title']}")
            return
    print(Fore.RED + f"[ERROR] Task #{task_id} not found.")


def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    original_len = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == original_len:
        print(Fore.RED + f"[ERROR] Task #{task_id} not found.")
        return
    save_tasks(tasks)
    print(Fore.YELLOW + f"[DELETED] Task #{task_id} removed.")


def main():
    parser = argparse.ArgumentParser(
        description="CLI Task Manager — Project 01/100",
        epilog="Example: python src/task_manager.py add 'Study Python' --priority high"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    add_parser.add_argument(
        "--priority", choices=["low", "medium", "high"],
        default="medium", help="Task priority (default: medium)"
    )

    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--all", action="store_true", help="Show completed tasks too"
    )

    done_parser = subparsers.add_parser("done", help="Mark a task complete")
    done_parser.add_argument("id", type=int, help="Task ID to mark complete")

    del_parser = subparsers.add_parser("delete", help="Delete a task")
    del_parser.add_argument("id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.priority)
    elif args.command == "list":
        list_tasks(show_all=args.all)
    elif args.command == "done":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()