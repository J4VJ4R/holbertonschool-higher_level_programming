#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates applying
for a back-end position with multiple technical challenges
, like this one:
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    user = sys.argv[2]

    url = "https://api.github.com/repos/" + user + "/" + repo + \
          "/commits?page=1&per_page=10"
    repos = requests.get(url)

    for element in repos.json():
        print("{}: {}".format(element.get("sha"),
                              element.get("commit").get("author").get("name")))
