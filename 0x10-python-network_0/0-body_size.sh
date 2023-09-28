#!/bin/bash

# Bash script to accept a URL as command line argument, make request to the given URL and print the body size of response

# Validate if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Make the request using curl and display the response body's size in bytes
content_length=$(curl -sI "$URL" | grep -i "Content-Length" | awk '{print $2}')
echo "Response body's size: ${content_length} bytes"
