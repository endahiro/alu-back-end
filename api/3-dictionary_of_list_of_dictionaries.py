#!/usr/bin/python3
"""Script that exports TODO lists of all employees to JSON."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_url = "{}/users".format(base_url)
    users = requests.get(users_url).json()

    # Get all todos
    todos_url = "{}/todos".format(base_url)
    todos = requests.get(todos_url).json()

    # Map user_id -> username
    users_dict = {}
    for user in users:
        users_dict[user.get("id")] = user.get("username")

    all_tasks = {}

    for todo in todos:
        user_id = todo.get("userId")
        if user_id not in all_tasks:
            all_tasks[user_id] = []

        task_dict = {
            "username": users_dict.get(user_id),
            "task": todo.get("title"),
            "completed": todo.get("completed")
        }
        all_tasks[user_id].append(task_dict)

    # Convert keys to strings for JSON, to match project style
    all_tasks_str_keys = {str(k): v for k, v in all_tasks.items()}

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(all_tasks_str_keys, jsonfile)

