#!/usr/bin/python3
""" 2-export_to_JSON

    Export data in the JSON format.
"""
import json
import requests
import sys


def main():
    """According to user_id, export information in json
    """
    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()
    tasks = []

    with open('{}.json'.format(user_id), 'w+') as file:
        for todo in request_todo:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": name}
            tasks.append(task)
        info = {user_id: tasks}
        file.write(json.dumps(info))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
