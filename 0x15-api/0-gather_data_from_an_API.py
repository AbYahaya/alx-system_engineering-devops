#!/usr/bin/python3
"""

Collecting request from an API

"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Base URL of the REST API
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Error fetching user data")
        return

    user = user_response.json()
    employee_name = user.get('name')

    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print("Error fetching TODO list data")
        return

    todos = todos_response.json()

    # Calculate the number of done and total tasks
    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as employee ID")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
