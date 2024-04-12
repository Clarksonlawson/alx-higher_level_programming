#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Sending a GET request to the provided URL and displaying the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

