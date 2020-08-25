#!/usr/bin/python3
"""
Write a Python script that takes your Github credentials
(username and password) and uses the Github API to display
your id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(user, token))
    print(r.json().get("id"))
