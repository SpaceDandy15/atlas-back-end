#!/usr/bin/python3
'''
A script that uses a provided API to fetch an employee by
their ID and returns the information found about their todo list progress in
the CSV data format.

- Records all tasks owned by the given employee
- Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- Output filename: `USER_ID.csv`
'''

import csv
import requests
from sys import argv


def process_request():
    '''
    Takes an integer representing an employee ID from argv and writes the found
    employee's todo list data in CSV format to a file.
    ----
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    ----
    '''
    # Check if employee ID is provided
    if len(argv) < 2:
        print("No employee ID provided")
        return

    # Retrieve the employee ID from command-line arguments
    given_id = argv[1]
    try:
        given_id = int(given_id)  # Convert to integer
    except ValueError:
        print("Invalid employee ID provided")
        return

    # Fetch employee data using the API
    employee_url = f"https://jsonplaceholder.typicode.com/users/{given_id}"
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={given_id}"

    employee_response = requests.get(employee_url)
    tasks_response = requests.get(tasks_url)

    # Check if both GET requests were successful
    if employee_response.status_code != 200 or tasks_response.status_code != 200:
        print("One or more GET requests failed")
        return

    # Parse the JSON data
    employee_data = employee_response.json()
    tasks_data = tasks_response.json()

    # Get the employee's username
    username = employee_data.get("username")

    # Create the CSV file with the employee's ID as the filename
    csv_filename = f"{given_id}.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task's details to the CSV file
        for task in tasks_data:
            task_completed = task["completed"]
            task_title = task["title"]
            csv_writer.writerow([given_id, username, task_completed, task_title])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    process_request()
