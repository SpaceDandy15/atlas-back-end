#!/usr/bin/python3
'''
A Python script that interfaces with an API to fetch all employees and
their todo tasks, formats the found data, and writes it into a `.json` file.

- Output filename: `todo_all_employees.json`
- Format per user (with collapsed whitespace):
    { "USER_ID": [
        {
        "task": "TASK_TITLE",
        "completed": "TASK_COMPLETED_STATUS",
        "username": "USERNAME"
        }, {
        "task": "TASK_TITLE",
        "completed": "TASK_COMPLETED_STATUS",
        "username": "USERNAME"
        }, ...
    ]}
'''

import json
import requests


def fetch_data():
    """
    Fetch all employees and their tasks from the API.

    Returns:
        list: A list of dictionaries, each containing task data.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch employee data
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch task data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return users_data, todos_data


def format_data(users_data, todos_data):
    """
    Format the fetched data into a dictionary of tasks by user ID.

    Args:
        users_data (list): List of employee data (user details).
        todos_data (list): List of task data.

    Returns:
        dict: A dictionary where each key is a user ID, and each value is a list of task dictionaries.
    """
    user_tasks = {}

    # Iterate through all tasks and group them by user ID
    for task in todos_data:
        user_id = str(task['userId'])  # Convert user ID to string
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": next(user['username'] for user in users_data if user['id'] == task['userId'])
        }

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append(task_data)

    return user_tasks


def save_to_json(data, filename="todo_all_employees.json"):
    """
    Save the formatted task data into a JSON file.

    Args:
        data (dict): The formatted task data to save.
        filename (str): The name of the output file. Default is "todo_all_employees.json".
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def main():
    """
    Main function to fetch, format, and save the data.
    """
    users_data, todos_data = fetch_data()  # Fetch employee and task data
    formatted_data = format_data(users_data, todos_data)  # Format the data by user
    save_to_json(formatted_data)  # Save the formatted data to a JSON file


if __name__ == "__main__":
    main()
