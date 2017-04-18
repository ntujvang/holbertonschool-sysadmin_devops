#!/usr/bin/python3
"""
Script uses a Rest API to retrieve todo list
-exports data into JSON format
"""
import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    r = requests.get(url)
    result = r.json()
    usr = result.get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    r = requests.get(url)
    result = r.json()
    lists = []
    data = {}
    with open(sys.argv[1] + '.json', 'w') as json_data:
        for item in result:
            temp_dict = {}
            if sys.argv[1] == str(item.get("userId")):
                status = item.get("completed")
                title = item.get("title")
                temp_dict.update({"task": title, "completed": status,
                                  "username": usr})
                lists.append(temp_dict)
        data[sys.argv[1]] = lists
        json.dump(data, json_data)
