# Todo CLI

A simple CLI project

## Description

Todo CLI is a lightweight command-line application for managing a list oftaskd. Tasks are stored in a text file and persist between program runs.

## Features

- Add a new task
- List all tasks with numbers
- Delete a task by its numbers
- Store tasks in a text file 
- Load the task file path from ".env"


## Tech stack

- python 3
- argparse
- python-dotenv
- Git & GitHub

Prerequisites
• Python 3.11 or later
• pip
• Git

Installation
Clone the repository and move into the project directory:
bash
git clone https://github.com/Mahdi-Ghasri/todo_cli.git
cd todo_cli

Create and activate a virtual environment:
bash
python -m venv .venv

Windows PowerShell:
powershell
.\.venv\Scripts\Activate.ps1

Install the required dependencies:
bash
pip install -r requirements.txt

Create a .env file based on .env.example and set the task file path:
env
TASKS_FILE=tasks.txt

Usage
Add a task
bash
python todo_cli.py add "Buy milk"

List tasks
bash
python todo_cli.py list

Delete a task
bash
python todo_cli.py delete 1

Data Storage
Tasks are stored locally in tasks.txt.
The .env file is used to configure the task file path. The .env file and task data are excluded from Git using .gitignore.
License
This project is created as part of a Python learning project.