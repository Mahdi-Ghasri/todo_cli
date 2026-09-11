markdown
# Quickstart

## 1. Create a virtual environment

```powershell
python -m venv .venv

2. Activate the virtual environment
powershell
.\.venv\Scripts\Activate.ps1

3. Install dependencies
powershell
pip install -r requirements.txt

4. Create the environment file
Create a .env file in the project root:
env
TASKS_FILE=tasks.txt

5. Add a task
powershell
python todo_cli.py add "Buy milk"

6. List tasks
powershell
python todo_cli.py list

7. Delete a task
powershell
python todo_cli.py delete 1

8. Check the result
Run:
powershell
python todo_cli.py list

The task list should be displayed with numbers.
