#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16.api.advanced"
    }
    params = {
        "limit": 10
    }
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    results = r.json().get("data")
    [print(a.get("data").get("title")) for a in results.get("children")]
