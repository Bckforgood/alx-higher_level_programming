#!/usr/bin/python3
"""
Python script that fetches a URL using the requests package
and displays the body response in a specified format.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request and retrieve the response
    response = requests.get(url)

    # Decode the response content and get the content type
    content = response.text
    content_type = type(content).__name__

    # Print the response in the desired format
    print("Body response:")
    print("    - type: {}".format(content_type))
    print("    - content: {}".format(content))
