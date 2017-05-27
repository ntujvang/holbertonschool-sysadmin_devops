#!/usr/bin/python3
"""
Prints the title of top 10 posts on a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    method to query API and get the top 10!
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': ""}
    r = requests.get(url, headers=header)
    if r.status_code != requests.codes.ok:
        print('None')
        return
    for i in range(0, 10):
        print(r.json()['data']['children'][i]['data']['title'])
