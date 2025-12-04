#!/usr/bin/python3
"""Script that uses a REST API to get TODO list progress of an employee."""
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
    employee_name = user.get("name")

    # Get todos for this user
    todos_url = "{}/todos".format(base_url)
    params = {"userId": employee_id}
    todos = requests.get(todos_url, params=params).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    # First line
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            number_of_done_tasks,
            total_tasks
        )
    )

    # Completed tasks titles
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
