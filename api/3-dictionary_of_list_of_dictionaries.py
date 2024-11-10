#!/usr/bin/python3
import json
import requests

def fetch_data():
    """
    Fetch task data from the JSONPlaceholder API.

    This function sends a GET request to the API to retrieve a list of tasks.
    The data is returned as a JSON response which is converted to a Python object.

    Returns:
        list: A list of dictionaries, where each dictionary represents a task.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    
    # If the request is successful (status code 200), return the response as a JSON object
    return response.json()

def format_data(tasks):
    """
    Format task data into a dictionary of user IDs with a list of their corresponding tasks.

    The data is grouped by 'userId', and each user’s tasks are structured into a dictionary
    that includes the username, task title, and completion status.

    Args:
        tasks (list): A list of tasks, where each task is a dictionary with details such as 'userId',
                      'title', and 'completed'.

    Returns:
        dict: A dictionary where the keys are user IDs (as strings) and the values are lists of task dictionaries.
    """
    user_tasks = {}

    for task in tasks:
        user_id = str(task["userId"])  # Convert the userId to string to match the desired format
        task_data = {
            "username": task["username"],
            "task": task["title"],
            "completed": task["completed"]
        }
        
        # Check if the userId already exists in the dictionary
        if user_id not in user_tasks:
            user_tasks[user_id] = []
        
        # Add the task data to the user's list of tasks
        user_tasks[user_id].append(task_data)

    return user_tasks

def save_to_json(data, filename="todo_all_employees.json"):
    """
    Save formatted task data to a JSON file.

    This function writes the provided data to a specified JSON file.

    Args:
        data (dict): The formatted data to save, typically a dictionary where each key represents
                     a user ID and the value is a list of task dictionaries.
        filename (str): The name of the JSON file where the data will be saved. Defaults to 'todo_all_employees.json'.
    """
    with open(filename, "w") as json_file:
        # Serialize the dictionary to JSON and write it to the file
        json.dump(data, json_file)

def main():
    """
    Main function to fetch, format, and save task data.

    This function coordinates the overall workflow by calling the functions to:
    1. Fetch task data from the API.
    2. Format the data into the required structure.
    3. Save the formatted data to a JSON file.
    """
    tasks = fetch_data()  # Step 1: Fetch the task data
    formatted_data = format_data(tasks)  # Step 2: Format the task data by user
    save_to_json(formatted_data)  # Step 3: Save the formatted data to a JSON file

if __name__ == "__main__":
    """
    The entry point of the script. It runs the main function if the script is executed directly.
    """
    main()
