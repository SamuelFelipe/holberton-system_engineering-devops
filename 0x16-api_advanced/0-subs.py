#!/usr/bin/python3

'''Use the reddit api'''
import requests


def number_of_subscribers(subreddit):
    '''return the nummber of subscribers'''
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url=url)

    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
