#!/usr/bin/python3
"""
All Users in json
"""

import json
import requests


def fetch_and_export_todo_data():
    # Base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        print("Error fetching user data")
        return

    users = users_response.json()

    # Dictionary to hold all tasks for all users
    all_todos = {}

    # Fetch TODO list data for each user
    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        todos_response = requests.get(f"{base_url}/todos?userId={user_id}")
        if todos_response.status_code != 200:
            print(f"Error fetching TODO list data for user ID {user_id}")
            continue

        todos = todos_response.json()

        # Store user's tasks in the dictionary
        all_todos[user_id] = [
            {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            for todo in todos
        ]

    # Create JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_todos, json_file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    fetch_and_export_todo_data()
