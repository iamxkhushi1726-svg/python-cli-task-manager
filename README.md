# Python CLI Task Manager

> Project 01/100 — Building a strong GitHub portfolio from scratch.

A lightweight command-line task manager built with Python. Supports adding, listing, completing, and deleting tasks with priority levels. Tasks persist across sessions using a local JSON file.

## Features

- Add tasks with low / medium / high priority
- View all pending tasks or include completed ones
- Mark tasks as done
- Delete tasks by ID
- Coloured terminal output using colorama
- Data stored in tasks.json (persists between runs)

## Tech Stack

- Python 3.x
- argparse (CLI interface)
- JSON (data storage)
- colorama (terminal colours)

## Installation

```bash
git clone https://github.com/iamxkhushi1726-svg/python-cli-task-manager.git
cd python-cli-task-manager
pip install -r requirements.txt
```

## Usage

```bash
# Add a task
python src/task_manager.py add "Your task title" --priority high

# List pending tasks
python src/task_manager.py list

# List all tasks including completed
python src/task_manager.py list --all

# Mark a task as done
python src/task_manager.py done 1

# Delete a task
python src/task_manager.py delete 2
```

## Example Output

```
--- Your Tasks ---
[TODO] #1 Learn Python argparse | HIGH | 2026-06-21 10:30
[TODO] #2 Push first project to GitHub | HIGH | 2026-06-21 10:31
[DONE] #3 Read about JSON file storage | MEDIUM | 2026-06-21 10:32
```

## What I Learned

- How to build a CLI tool using Python argparse
- How to persist data using JSON file I/O
- How to structure a Python project with src/ layout
- How to use colorama for coloured terminal output

## Part of 100 Projects Challenge

This is project 01 of my 100-project challenge to build a strong GitHub portfolio
and secure AI/ML and software engineering internships.

Follow my progress: [GitHub Profile](https://github.com/iamxkhushi1726-svg)