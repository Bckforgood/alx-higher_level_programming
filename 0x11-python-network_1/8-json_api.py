#!/usr/bin/python3
"""
Python script that sends aas a parameter and processes the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Define the payload with the letter as a parameter
    payload = {'q': q}

    # Send a POST request and retrieve the response
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        if json_response:
            # Display the id and name
            print("[{}]".format(json_response.get('id')))
            print("{}".format(json_response.get('name')))

        else:
            print("No result")
    except ValueError:
        # Display an error if the response is not valid JSON
        print("Not a valid JSON")
