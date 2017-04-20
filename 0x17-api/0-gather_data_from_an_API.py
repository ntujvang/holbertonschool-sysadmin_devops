#!/usr/bin/python3
"""
Script uses a Rest API to retrieve todo list
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    r = requests.get(url)
    result = r.json()
    usr = result.get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    r = requests.get(url)
    total = 0
    done = 0
    tasks = []
    for task in r.json():
        if task.get("completed"):
            done += 1
            tasks.append(task.get("title"))
        total += 1

    print("Employee {} is done with tasks({}/{}):".format(usr, done, total))
    for name in tasks:
        print("\t {}".format(name))
