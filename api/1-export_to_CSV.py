#!/usr/bin/python3
""" 1-export_to_CSV

    Export data in the CSV format.
"""
import csv
import requests
import sys


def main():
    """According to user_id, export information in CSV
    """
    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()

    with open('{}.csv'.format(user_id), 'w+') as file:
        for todo in request_todo:
            info = '"{}","{}","{}","{}"\n'.format(
                user_id, name, todo.get('completed'), todo.get('title'))
            file.write(info)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
