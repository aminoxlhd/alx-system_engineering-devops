#!/usr/bin/python3
""" queries the Reddit API, parses the title of all hot articles """
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    user_agent = {'User-agent': 'Agent'}
    r = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                     .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if r.status_code == 200:
        rs = r.json()['data']
        aft = rs['after']
        rs = rs['children']
        for r in rs:
            title = r['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
