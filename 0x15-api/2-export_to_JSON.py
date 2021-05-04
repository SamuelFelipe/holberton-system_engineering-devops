#!/usr/bin/python3

'''
Use requests module to do a get requests from
https://jsonplaceholder.typicode.com/todos
and write the responce into a csv file
'''

if __name__ == '__main__':

    import json
    import requests
    from sys import argv

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    task_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'

    responce_user = requests.get(user_url.format(argv[1]))
    responce_task = requests.get(task_url.format(argv[1]))

    it = json.loads(responce_task.text)
    iu = json.loads(responce_user.text)
    out = {}

    out[argv[1]] = it

    with open('{}.json'.format(argv[1]), 'w') as f:
        f.write(json.dumps(out))
