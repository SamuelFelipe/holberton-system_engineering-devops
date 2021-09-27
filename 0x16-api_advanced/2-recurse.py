#!/usr/bin/python3

'''Use the reddit api'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''subreddit hot post'''

    if after is None:
        return hot_list

    url = 'https://reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(url=url, headers={'User-Agent': 'recurse'})

    if response.status_code != 200:
        return None

    inf = response.json()
    children = inf['data']['children']

    for post in children:
        hot_list.append(post['data']['title'])

    return recurse(subreddit, hot_list, inf['data']['after'])
