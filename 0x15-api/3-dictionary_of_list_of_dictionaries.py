#!/usr/bin/python3
""" This script writes information about all employees and their TODOs
    in a JSON format.

    API URL: https://jsonplaceholder.typicode.com/
    API endpoits: users/, todos
    Filename: todo_all_employees.json
"""
from json import dump
from requests import get
from sys import argv


def all_tasks_to_json():
    """ Writes information about all employees and their TODOs
        in a JSON format.
    """
    filename = "todo_all_employees.json"
    API_URL = "https://jsonplaceholder.typicode.com/"

    employees = get(API_URL + "users/").json()
    todos = get(API_URL + "todos/").json()

    json = {}
    for employee in employees:
        _id = employee.get("id")
        json[_id] = []
        for task in todos:
            if task.get("userId") == _id:
                json[_id].append({"username": employee.get("username"),
                                  "task": task.get("title"),
                                  "completed": task.get("completed")})
    del employees, todos

    with open(filename, 'w') as _file:
        dump(json, _file)


if __name__ == "__main__":
    all_tasks_to_json()
