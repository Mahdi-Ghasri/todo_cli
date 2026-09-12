import argparse
import os
from dotenv import load_dotenv

load_dotenv()
TASKS_FILE = os.getenv("TASKS_FILE")

if not TASKS_FILE:
    raise ValueError("TASKS_FILE is not set in the .env file.")

parser = argparse.ArgumentParser(description="A simple CLI project")

subparsers = parser.add_subparsers(dest="command" , required=True)

add_parser = subparsers.add_parser("add")
add_parser.add_argument("task")

subparsers.add_parser("list")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("task_number", type=int)




def load_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        tasks = file.read().splitlines()

        return tasks



def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(tasks))





def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)





def list_tasks():
    tasks = load_tasks()

    for index, task in enumerate(tasks, start=1):
        print(f"{index}, {task}")





def delete_task(task_number):
    tasks = load_tasks()

# Convert the user- facing task number to a zero-based list index.

    del tasks[task_number - 1]

    save_tasks(tasks)


args = parser.parse_args()

if args.command == "add":
    add_task(args.task)
elif args.command == "list":
    list_tasks()
elif args.command == "delete":
    delete_task(args.task_number)