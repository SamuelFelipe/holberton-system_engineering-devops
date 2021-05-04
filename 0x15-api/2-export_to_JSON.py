#!/usr/bin/python3

'''
Use requests module to do a get requests from
https://jsonplaceholder.typicode.com/todos
and write the responce into a csv file
'''

if __name__ == '__main__':

    import json
    import requests

    user_url = 'https://jsonplaceholder.typicode.com/users'
    task_url = 'https://jsonplaceholder.typicode.com/todos'

    responce_user = requests.get(user_url)
    responce_task = requests.get(task_url)

    it = json.loads(responce_task.text)
    iu = json.loads(responce_user.text)
    out = {}

    for i in it:
        try:
            out[i['userId']].append(
                            {"username": iu[i['userId'] - 1]['username'],
                             "task": i['title'],
                             "completed": i['completed']
                             }
                                    )
        except KeyError:
            out[i['userId']] = [{"username": iu[i['userId'] - 1]['username'],
                                 "task": i['title'],
                                 "completed": i['completed']
                                 }]

            with open('todo_all_employees.json', 'w') as f:
                f.write(json.dumps(out))
