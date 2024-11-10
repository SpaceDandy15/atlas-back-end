#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress for a given employee
using the JSONPlaceholder REST API.

It takes the employee ID as input and returns the following:

1. The employee's name.
2. The number of completed tasks vs the total number of tasks.
3. A list of completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    employee_id (int): ID of Employee whose TODO list you want to check

Example:
    python3 0-gather_data_from_an_API.py 1
"""
import requests
import sys


def get_todo_progress(employee_id):
    """Fetch and display employee TODO list progress."""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO tasks data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate total tasks and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = [
        task['title'] for task in todos_data if task['completed']]

    # Output the progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_todo_progress(employee_id)
