#!/usr/bin/python3
"""
This script retrieves and exports the TODO list progress for a given employee
using the JSONPlaceholder REST API into a JSON file.

Takes the employee ID as input and creates a JSON file in the following format:

{
    "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        ...
    ]
}

The file name will be the employee ID (USER_ID.json).

Usage:
    python3 2-export_to_JSON.py <employee_id>

Arguments:
    employee_id (int): ID of Employee whose TODO list you want to export

Example:
    python3 2-export_to_JSON.py 2
"""

import json
import requests
import sys


def get_todo_data(employee_id):
    """Fetch and export employee TODO list progress to JSON."""
    # URLs to fetch employee and TODO data
    user_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )

    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO tasks data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a dictionary to store the tasks
    tasks = []
    for task in todos_data:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        }
        tasks.append(task_info)

    # Create the final structure with employee_id as the key
    data = {str(employee_id): tasks}

    # Create a JSON file with employee_id as the filename
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)

    print(f"Data exported to {json_filename}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_todo_data(employee_id)
