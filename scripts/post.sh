#!/bin/bash

# Usage: ./post.sh <token> <username> <text>

token=$1
username=$2
text=$3

payload=$(jq -n --arg username "$username" --arg text "$text" '{userName: $username, text: $text}')

curl -v \
  -H "Content-Type:application/json" \
  -H "authorization:${token}" \
  --request POST \
  --data "${payload}" \
  http://thwopzap.net/api/messages
