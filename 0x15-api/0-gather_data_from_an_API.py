#!/usr/bin/python3
"""
This is for the api task
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee information
    user_url = f'{base_url}/users/{employee_id}'
    response_user = requests.get(user_url)

    if response_user.status_code != 200:
        print(f"Error: Unable to fetch user with ID {employee_id}")
        return

    user_data = response_user.json()
    em_name = user_data.get('name')

    # Fetch employee's TODO list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    response_todos = requests.get(todos_url)

    if response_todos.status_code != 200:
        print(f"Error: Unable to fetch TODO for user with ID {employee_id}")
        return

    todos_data = response_todos.json()

    # Calculate TODO list progress
    tot_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    tasks_num = len(done_tasks)

    # Print the TODO list progress
    print(f"Employee {em_name} is done with tasks({tasks_num}/{tot_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
