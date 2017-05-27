#!/usr/bin/python3
"""
Recursively finding the top 10!
"""
import requests


def recurse(subreddit, hot_list=[], new_str=""):
    """
    using recursion to get top 10!
    """
    if (new_str is None):
        return hot_list
    if (len(hot_list) == 0):
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, new_str)
    header = {'User-Agent': ""}
    r = requests.get(url, headers=header)
    if r.status_code != requests.codes.ok:
        return None
    elif 'data' not in r.json():
        return None
    else:
        for item in r.json()['data']['children']:
            hot_list.append(item['data']['title'])
    new_str = r.json()['data']['after']
    return recurse(subreddit, hot_list, new_str)
