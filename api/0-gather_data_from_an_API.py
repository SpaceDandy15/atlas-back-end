#!/usr/bin/python3

import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches and displays the TODO list progress of an employee based on their ID.
    
    Parameters:
    employee_id (int): The ID of the employee whose TODO list progress will be retrieved.
    
    The function makes two requests to the JSONPlaceholder API:
    - One to retrieve employee information (name) from the user endpoint.
    - Another to retrieve TODO tasks associated with the employee from the todos endpoint.
    
    Output:
    The function outputs the employee's TODO list progress to the console in the format:
    - First line: "Employee <EMPLOYEE_NAME> is done with tasks(<NUMBER_OF_DONE_TASKS>/<TOTAL_NUMBER_OF_TASKS>):"
    - Following lines: Titles of completed tasks, each preceded by a tab and a space.
    """
    
    # API endpoint URLs for fetching user info and TODOs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    # Fetch employee information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        # If user ID is invalid or not found, output a message and stop
        print("User not found.")
        return
    
    # Parse employee data to retrieve name
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Fetch employee's TODO tasks
    todos_response = requests.get(todos_url)
    todos = todos_response.json()  # List of TODO items for the employee
    
    # Calculate total tasks and number of completed tasks
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    
    # Display the employee's TODO list progress in the required format
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        # Print each completed task's title with a tab and space prefix
        print("\t " + task.get('title'))

if __name__ == "__main__":
    # Check if the script received exactly one command-line argument (employee ID)
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Attempt to convert the command-line argument to an integer (employee ID)
    try:
        employee_id = int(sys.argv[1])
        fetch_todo_list_progress(employee_id)
    except ValueError:
        # Output error if the employee ID is not a valid integer
        print("Employee ID must be an integer.")
