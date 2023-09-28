#!/bin/bash

# This script takes a URL, sends a request using curl, and displays the size of the response body in bytes

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send the request using curl, follow redirects, and display the size of the response body in bytes
curl -sL "$URL" | wc -c

