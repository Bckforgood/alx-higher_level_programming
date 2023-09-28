#!/bin/bash

# This script takes a URL and displays the size of the response body in bytes

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send the request and display the size of the response body in bytes
curl -sI "$URL" | grep -i "Content-Length" | awk '{print $2}'
