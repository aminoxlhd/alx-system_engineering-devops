#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
	url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
	headers = {'User-Agent': 'My_User_Agent'}
	r = requests.get(url, headers=headers)
	if r.status_code == 200:
		data = r.json()
		return data.get('data').get('subscribers')
	else:
		return 0
