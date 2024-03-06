#!/usr/bin/python3
""" queries  the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        sub = data['data']['subscribers']
        return sub
    else:
        return 0
