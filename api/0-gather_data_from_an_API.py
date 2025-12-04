#!/usr/bin/python3
"""Script that uses a REST API to get TODO list progress of an employee."""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = "{}/users/{}".format(base_url, employee_id)
    user = requests.get(user_url).json()
    employee_name = user.get("name")

    # Get todos for this user
    todos_url = "{}/todos".format(base_url)
    todos = requests.get(
        todos_url,
        params={"userId": employee_id}
    ).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            len(done_tasks),
            total_tasks
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
