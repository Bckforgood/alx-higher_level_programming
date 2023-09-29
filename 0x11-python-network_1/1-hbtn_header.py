#!/usr/bin/python3
"""
Python script that takes a URL, sends a request, and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Extract the URL from the command-line arguments

    # Send a request and retrieve the response headers
    with urllib.request.urlopen(url) as response:
        # Retrieve and display the value of the X-Request-Id header
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
