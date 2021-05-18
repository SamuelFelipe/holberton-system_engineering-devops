#!/usr/bin/python3

'''
Use the reddit Api to get information.
'''
import requests


def top_ten(subreddit):
    '''Return the top 10 post in a subreddit'''

    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url=url)

    if response.status_code != 200:
        print(None)
        return

    children = response.json()['data']['children']

    for post in range(10):
        print(children[post]['data']['title'])
