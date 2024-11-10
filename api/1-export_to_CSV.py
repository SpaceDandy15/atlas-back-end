#!/usr/bin/python3
"""
This script retrieves and exports the TODO list progress for a given employee
using the JSONPlaceholder REST API into a CSV file.

Takes the employee ID as input and creates a CSV file in the following format:

"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

The file name will be the employee ID (USER_ID.csv).

Usage:
    python3 1-export_to_CSV.py <employee_id>

Arguments:
    employee_id (int): ID of Employee whose TODO list you want to export

Example:
    python3 1-export_to_CSV.py 2
"""

import requests
import sys
import csv


def get_todo_data(employee_id):
    """Fetch and export employee TODO list progress to CSV."""
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

    # Create a CSV file with employee_id as the filename
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the CSV header
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )

        # Write the task details for each task
        for task in todos_data:
            task_completed = task['completed']
            task_title = task['title']
            writer.writerow([employee_id, employee_name,
                             task_completed, task_title])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_todo_data(employee_id)
