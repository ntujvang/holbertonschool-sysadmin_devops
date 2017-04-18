#!/usr/bin/python3
"""
Script uses a Rest API to retrieve todo list
- exports data in CSV format
"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    r = requests.get(url)
    result = r.json()
    usr = result.get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    r = requests.get(url)
    result = r.json()
    with open(sys.argv[1] + '.csv', 'w') as csv_data:
        file = csv.writer(csv_data, quoting=csv.QUOTE_ALL)
        for item in result:
            if sys.argv[1] == str(item.get("userId")):
                status = item.get("completed")
                title = item.get("title")
                file.writerow([sys.argv[1], usr, status, title])
