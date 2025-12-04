#!/usr/bin/python3
"""Script that exports an employee's TODO list to JSON."""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = "{}/users/{}".format(base_url, employee_id)
    user = requests.get(user_url).json()
    username = user.get("username")

    # Get todos for this user
    todos_url = "{}/todos".format(base_url)
    params = {"userId": employee_id}
    todos = requests.get(todos_url, params=params).json()

    tasks_list = []

    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks_list}

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)

