#!/usr/bin/python3
""" This script returns information about employee's TODO list progress
    for a given employee ID.

    API URL: https://jsonplaceholder.typicode.com/
    API endpoits: users/, todos
"""
import csv
from requests import get
from sys import argv


def list_tasks(employee_id=None):
    """ Returns information about employee's TODO list progress
        for a given employee ID.
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
