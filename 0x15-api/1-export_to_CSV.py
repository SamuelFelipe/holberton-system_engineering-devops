#!/usr/bin/python3

'''
Use requests module to do a get requests from
https://jsonplaceholder.typicode.com/todos
and write the responce into a csv file
'''

if __name__ == '__main__':

    from sys import argv
    import json
    import requests

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'
    user_id = argv[1]
    out = '"{}","{}","{}","{}"\n'

    responce_user = requests.get(user_url.format(user_id))
    responce_task = requests.get(task_url.format(user_id))

    info_task = json.loads(responce_task.text)
    info_user = json.loads(responce_user.text)

    with open('{}.csv'.format(argv[1]), 'w') as f:
        for i in info_task:
            f.write(out.format(argv[1], info_user['username'],
                    i['completed'], i['title']))
