#!/usr/bin/python3
"""
This is for the api task
"""

from requests import get
from sys import argv


if __name__ == '__main__':
    usr_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr_id)
    response = get(url)
    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(usr_id)
    response = get(url)
    tasks = response.json()
    with open('{}.csv'.format(usr_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, task.get('completed'),
                               task.get('title')))
