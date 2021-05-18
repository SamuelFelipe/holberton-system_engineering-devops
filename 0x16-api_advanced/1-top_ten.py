#!/usr/bin/python3

'''Use the reddit api'''
import requests


def top_ten(subreddit):
    '''return the top ten hot post'''
    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url=url)
    
    if response.status_code != 200:
        print(None)
        return

    for post in response.json()['data']['children']:
        print(post['data']['title'])
