#!/usr/bin/python3
"""
Script uses a Rest API to retrieve todo list
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    r = requests.get(url)
    result = r.json()

    holder = {}
    for user in result:
        tasks = []
        api = "https://jsonplaceholder.typicode.com"
        url_2 = api + "/users/{}/todos".format(user.get("id"))
        r_2 = requests.get(url_2)
        for item in r_2.json():
            temp = {}
            temp["task"] = item.get("title")
            temp["completed"] = item.get("completed")
            temp["username"] = user.get("username")
            tasks.append(temp)
        holder[user.get("id")] = tasks
    with open("todo_all_employees.json", 'w') as json_data:
        json.dump(holder, json_data)
