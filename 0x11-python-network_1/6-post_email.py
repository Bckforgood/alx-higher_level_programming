#!/usr/bin/python3
"""
Python script that sends a POST request with an email as a parameter
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Extract the URL from the command-line arguments
    email = sys.argv[2]  # Extract the email from the command-line arguments

    # Define the payload with the email as a parameter
    payload = {'email': email}

    # Send a POST request and retrieve the response
    response = requests.post(url, data=payload)

    # Print the response body
    print("Your email is: {}".format(response.text))
