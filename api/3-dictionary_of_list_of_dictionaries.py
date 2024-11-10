#!/usr/bin/python3
"""
This module fetches tasks from a public API (JSONPlaceholder),
formats them by user, and saves the formatted data into a JSON file.

Functions:
    fetch_data: Fetches task data from the API.
    format_data: Formats task data into a user-centered dictionary.
    save_to_json: Saves formatted task data into a JSON file.
    main: Orchestrates the flow of fetching, formatting, and saving task data.
"""

import json
import requests


def fetch_data():
    """
    Fetch task data from the JSONPlaceholder API.

    Returns:
        list: A list of dictionaries representing tasks.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    return response.json()


def format_data(tasks):
    """
    Format task data into a dictionary by user ID.

    Args:
        tasks (list): List of task dictionaries.

    Returns:
        dict: each key is a user ID, and value is a list of task dictionaries.
    """
    user_tasks = {}

    for task in tasks:
        user_id = str(task["userId"])
        task_data = {
            "username": task["username"],
            "task": task["title"],
            "completed": task["completed"]
        }

        if user_id not in user_tasks:
            user_tasks[user_id] = []

        user_tasks[user_id].append(task_data)

    return user_tasks


def save_to_json(data, filename="todo_all_employees.json"):
    """
    Save formatted task data to a JSON file.

    Args:
        data (dict): Formatted task data.
        filename (str): The file name to save the data to
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


def main():
    """
    Main function to fetch, format, and save task data.
    """
    tasks = fetch_data()
    formatted_data = format_data(tasks)
    save_to_json(formatted_data)


if __name__ == "__main__":
    main()
