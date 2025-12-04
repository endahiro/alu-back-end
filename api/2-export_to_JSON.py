#!/usr/bin/python3
"""Export an employee's TODO list to JSON."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = "{}/users/{}".format(base_url, employee_id)
    user = requests.get(user_url).json()
    username = user.get("username")

    # Get todos for this user
    todos_url = "{}/todos".format(base_url)
    todos = requests.get(
        todos_url,
        params={"userId": employee_id}
    ).json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {employee_id: tasks}

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)
