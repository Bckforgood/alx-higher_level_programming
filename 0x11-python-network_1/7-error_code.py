#!/usr/bin/python3
"""
Python script tha and displays the body of the response.
Prints an error message  if it's greater than or equal to 400.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Extract the URL from the command-line arguments

    # Send a GET request and retrieve the response
    response = requests.get(url)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        # Print the response body
        print(response.text)
