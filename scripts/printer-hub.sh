#!/bin/bash

# API URL
url="http://thwopzap.net/api/messages"

# Static token for authentication
auth_token="secret123"

username="Jerome"

# Function to send a message
send_message() {
  echo "Enter your message:"
  read message

# if user is not set, ask for username
if [ -z "$username" ]; then
  echo "Enter your username:"
  read username
fi

  # Convert message and username to JSON format
  json_payload=$(jq -n \
    --arg user "$username" \
    --arg msg "$message" \
    '{text: $msg, userName: $user}')

  # Send POST request to the API
  response=$(curl -X POST $url \
    -H "Content-Type: application/json" \
    -H "Authorization: $auth_token" \
    -d "$json_payload")

  echo "Response from server: $response"
}

# Function to get messages
get_messages() {
  # Send GET request to the API
  response=$(curl -s -X GET $url \
    -H "Authorization: $auth_token")

  echo $response | jq -r '.[] | "\(.userName): \(.text) [\(.createdAt)]"'
}

# Check command argument
case "$1" in
  send)
    send_message
    ;;
  get)
    get_messages
    ;;
  *)
    echo "Usage: printer-hub [get|send]"
    exit 1
    ;;
esac
