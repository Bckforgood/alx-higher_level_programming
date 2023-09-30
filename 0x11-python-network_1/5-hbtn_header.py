#!/usr/bin/python3
"""
Python script that takes a URL, sends a request, and displays the value of
the X-Request-Id variable found in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Extract the URL from the command-line arguments

    # Send a GET request and retrieve the response
    response = requests.get(url)

    # Retrieve and display the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
