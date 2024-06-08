#!/usr/bin/python3
"""
Using CSV to deliver an API response
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("Error fetching user data")
        return

    user = user_response.json()
    employee_name = user.get('username')

    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print("Error fetching TODO list data")
        return

    todos = todos_response.json()

    # Create CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, employee_name,
                            todo.get('completed'), todo.get('title')])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as employee ID")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
