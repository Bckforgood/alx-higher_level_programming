#!/usr/bin/python3
"""
Python script that sends a POST request to a URL with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Extract the URL from the command-line arguments
    email = sys.argv[2]  # Extract the email from the command-line arguments

    # Encode the email to be sent as a parameter in the request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request and retrieve the response
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        response_body = response.read().decode('utf-8')

        # Print the response body
        print(response_body)
