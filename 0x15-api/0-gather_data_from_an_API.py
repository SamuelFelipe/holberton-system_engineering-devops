#!/usr/bin/python3

'''
Print an api responce
'''

if __name__ == '__main__':

    from sys import argv
    import json
    import requests

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'
    user_id = argv[1]
    out = 'Employee {} is done with tasks({}/{}):{}'

    responce_user = requests.get(user_url.format(user_id))
    responce_task = requests.get(task_url.format(user_id))
    completed = 0

    info_task = json.loads(responce_task.text)
    info_user = json.loads(responce_user.text)
    titles = ''

    try:
        for i in info_task:
            if i['completed']:
                completed += 1
                titles += '\n\t ' + i['title']

        print(out.format(info_user['name'], completed, len(info_task), titles))
    except Exception:
        pass
