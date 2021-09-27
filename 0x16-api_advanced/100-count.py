#!/usr/bin/python3

'''Use the reddit api'''
import requests


def count_words(subreddit, word_list, after='', count={}):

    if after is None:
        return count

    url = 'https://reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(url=url, headers={'User-Agent': 'vert'})

    if response.status_code != 200:
        return None

    inf = response.json()
    children = inf['data']['children']

    for post in children:
        for word in word_list:
            if count.get(word):
                count[word.casefold()] += len(post['data']['title']
                                              .casefold()
                                              .split((word + ' ')
                                              .casefold())) - 1
            else:
                count[word.casefold()] = len(post['data']['title']
                                             .casefold().split((word + ' ')
                                             .casefold())) - 1

    result = count_words(subreddit, word_list, inf['data']['after'], count)
    if result:
        for val in sorted(result.items(), key=lambda item: item[0]):
            print('{}: {}'.format(*val))
        result = None
    return result
