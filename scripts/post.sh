#!/bin/bash

# Usage: ./post.sh <token> <username> <message>

token=$1
username=$2
message=$3

payload=$(jq -n --arg username "$username" --arg message "$message" '{userName: $username, message: $message}')

curl -v \
  -H "Content-Type:application/json" \
  -H "authorization:${token}" \
  --request POST \
  --data "${payload}" \
  http://78.47.100.184/api/messages
