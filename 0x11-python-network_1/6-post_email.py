#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.


"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}

    if url is not None:
        response = requests.post(url, data=payload)
        print(response.text)
