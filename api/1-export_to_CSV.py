#!/usr/bin/python3
"""Export an employee's TODO list to CSV."""
import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
