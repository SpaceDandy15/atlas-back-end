#!/usr/bin/python3
"""
This module fetches tasks from a public API (JSONPlaceholder),
formats them by user, and saves the formatted data into individual JSON files
for each user.

Usage:
    python3 2-export_to_JSON.py <employee_id>

Arguments:
    employee_id (int): ID of the Employee whose tasks you want to export
"""

import json
import requests
import sys


def fetch_data():
    """
    Fetch task data from the JSONPlaceholder API.

    Returns:
        list: A list of dictionaries representing tasks.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    # Error handling for failed request
    if response.status_code != 200:
        print("Error: Failed to fetch tasks data.")
        return None

    return response.json()


def format_data(tasks, employee_id):
    """
    Format task data into a list of tasks for a specific user.

    Args:
        tasks (list): List of task dictionaries.
        employee_id (int): The employee ID to filter the tasks for.

    Returns:
        list: A list of task dictionaries for the given employee ID.
    """
    employee_tasks = []

    for task in tasks:
        if task['userId'] == employee_id:
            task_data = {
                "username": task["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            employee_tasks.append(task_data)

    return employee_tasks


def save_to_json(data, employee_id):
    """
    Save the task data for a specific employee to a JSON file.

    Args:
        data (list): Task data to save.
        employee_id (int): Employee ID used for the filename.
    """
    filename = f"{employee_id}.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump({employee_id: data}, json_file)

    print(f"Data exported to {filename}.")


def process_request(employee_id):
    """
    Process request to fetch, format, save task data for a given employee ID.

    Args:
        employee_id (int): The employee ID for the tasks to fetch.
    """
    tasks = fetch_data()

    if tasks is None:
        return

    # Format the data for the specific employee
    formatted_data = format_data(tasks, employee_id)

    # Save the formatted data to a JSON file
    save_to_json(formatted_data, employee_id)


def main():
    """
    Main function to orchestrate fetching, formatting, and saving the data
    for an employee's tasks.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid employee ID provided.")
        return

    process_request(employee_id)


if __name__ == "__main__":
    main()
