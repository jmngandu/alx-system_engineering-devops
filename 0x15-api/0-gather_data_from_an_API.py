#!/usr/bin/python3
""" getting data from an API"""
import sys
import requests


if __name__ == "__main__":
    id = sys.argv[1]
    tasks = []
    complete = 0
    total_tasks = 0
    url = "https://jsonplaceholder.typicode.com/users/" + id
    res = requests.get(url).json()
    name = res.get('name')
    url = "https://jsonplaceholder.typicode.com/todos"
    res_tasks = requests.get(url).json()

    for i in res_tasks:
        if i.get("userId") == int(id):
            if i.get("completed") is True:
                tasks.append(i["title"])
                complete += 1
        total_tasks += 1
    print("Employee {} is done with tasks ({}/{}):"
          .format(name, complete, total_tasks))

    for x in tasks:
        print("\t {}".format(x))
