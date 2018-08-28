#!/usr/bin/python3
""" This script writes information about employee's TODO list
    for a given employee ID to a file in CSV format.

    API URL: https://jsonplaceholder.typicode.com/
    API endpoits: users/, todos

    Attributes:
        @argv[1]: employee_id, int
"""
import csv
from requests import get
from sys import argv


def list_tasks(employee_id=None):
    """ Writes information about employee's TODO list
        for a given employee ID to a file in CSV format.

        Attributes:
            @employee_id: ID of the employee, int
    """
    try:
        _id = int(employee_id)
    except:
        return

    filename = employee_id + ".csv"
    API_URL = "https://jsonplaceholder.typicode.com/"

    employee = get(API_URL + "users/{:d}".format(_id)).json()
    todos = get(API_URL + "todos?userId={:d}".format(_id)).json()

    uname = employee.get("username")
    del employee

    with open(filename, "w") as _file:
        w = csv.writer(_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            w.writerow([_id, uname, task.get("completed"), task.get("title")])


if __name__ == "__main__":
    list_tasks(argv[1])
