#!/usr/bin/python3
"""
Query reddit API for # of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    get the number of subscribers from a subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': ""}
    r = requests.get(url, headers=header)
    if r.status_code != requests.codes.ok:
        return (0)
    subs = r.json()['data'].get('subscribers', 0)
    return subs
