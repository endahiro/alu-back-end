#!/usr/bin/python3
"""Export TODO lists of all employees to JSON."""
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

    # Map user id (as string) -> username
    usernames = {}
    for user in users:
        user_id = str(user.get("id"))
        usernames[user_id] = user.get("username")

    all_tasks = {}

    for todo in todos:
        user_id = str(todo.get("userId"))
        if user_id not in all_tasks:
            all_tasks[user_id] = []
        all_tasks[user_id].append({
            "username": usernames.get(user_id),
            "task": todo.get("title"),
            "completed": todo.get("completed")
        })

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
