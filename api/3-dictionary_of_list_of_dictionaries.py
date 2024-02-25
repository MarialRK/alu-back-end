#!/usr/bin/python3
""" 3-dictionary_of_list_of_dictionaries

    Export data in the JSON format.
"""
import json
import requests


def main():
    """According to user_id, export information in json
    """
    users_uri = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_uri).json()
    info = {}

    for user in users:
        user_id = user.get('id')
        name = user.get('username')
        todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id)
        request_todo = requests.get(todos).json()
        tasks = []
        for todo in request_todo:
            task = {"username": name, "task": todo.get("title"),
                    "completed": todo.get("completed")}
            tasks.append(task)
        info[user_id] = tasks

    with open('todo_all_employees.json', 'w+') as file:
        file.write(json.dumps(info))


if __name__ == "__main__":
    main()
