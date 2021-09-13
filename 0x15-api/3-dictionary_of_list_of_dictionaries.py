#!/usr/bin/python3

'''
wrinfo_taske an api responce into a csv file
'''

if __name__ == '__main__':

    import json
    import requests

    user_url = 'https://jsonplaceholder.typicode.com/users'
    task_url = 'https://jsonplaceholder.typicode.com/todos'

    responce_user = requests.get(user_url)
    responce_task = requests.get(task_url)

    info_task = json.loads(responce_task.text)
    info_user = json.loads(responce_user.text)
    out = {}

    print(info_task)

    for i in info_task:
        try:
            out[i['userId']].append(
                            {"username":
                             info_user[i['userId'] - 1]['username'],
                             "task": i['title'],
                             "completed": i['completed']
                             }
                                    )
        except KeyError:
            out[i['userId']] = [{"username":
                                 info_user[i['userId'] - 1]['username'],
                                 "task": i['title'],
                                 "completed": i['completed']
                                 }]

            with open('todo_all_employees.json', 'w') as f:
                f.write(json.dumps(out))
