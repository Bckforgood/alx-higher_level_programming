#!/usr/bin/python3
"""
Python script that sends a request to a URL and displays the body of the response.
Handles urllib.error.HTTPError exceptions and prints the HTTP status code in case of an error.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Extract the URL from the command-line arguments

    try:
        # Send a request and retrieve the response
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')

            # Print the response body
            print(response_body)
    except urllib.error.HTTPError as e:
        # Print the error code in case of an HTTP error
        print("Error code:", e.code)
