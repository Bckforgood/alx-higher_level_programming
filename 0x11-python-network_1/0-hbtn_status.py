#!/usr/bin/python3
"""
Python script that fetches a URL using urllib package
and displays the body response in a specified format.
"""

import urllib.request

def fetch_and_display_response(url):
    """
    Fetches the URL using urllib and displays the body response.
    
    Parameters:
        url (str): The URL to fetch.
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print("    - type: {}".format(type(content)))
        print("    - content: {}".format(content.decode('utf-8')))
        print("    - utf8 content: {}".format(utf8_content))

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_and_display_response(url)
