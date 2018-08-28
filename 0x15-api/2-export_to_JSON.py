#!/usr/bin/python3
""" This script writes information about employee's TODO list
    for a given employee ID to a file in a JSON format.

    API URL: https://jsonplaceholder.typicode.com/
    API endpoits: users/, todos
    Filename: "<employee_id>.json"

    Arguments:
        @argv[1]: employee_id, int
"""
from json import dump
from requests import get
from sys import argv


def list_tasks(employee_id=None):
    """ Writes information about employee's TODO list
        for a given employee ID to a file in a JSON format.

        Arguments:
            @employee_id: ID of the employee, int
    """
    try:
        _id = int(employee_id)
    except:
        return

    filename = employee_id + ".json"
    API_URL = "https://jsonplaceholder.typicode.com/"

    employee = get(API_URL + "users/{:d}".format(_id)).json()
    todos = get(API_URL + "todos?userId={:d}".format(_id)).json()

    uname = employee.get("username")
    del employee

    json = {employee_id: []}
    for task in todos:
        json[employee_id].append({"task": task.get("title"),
                                  "completed": task.get("completed"),
                                  "username": uname})
    del todos

    with open(filename, "w") as _file:
        dump(json, _file)


if __name__ == "__main__":
    list_tasks(argv[1])
