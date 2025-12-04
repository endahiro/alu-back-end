#!/usr/bin/python3
"""Script that exports an employee's TODO list to CSV."""
import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
