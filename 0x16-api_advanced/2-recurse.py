#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the
titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code == 404:
        return None

    res = r.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for a in res.get("children"):
        hot_list.append(a.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
