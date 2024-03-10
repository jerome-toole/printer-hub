#!/bin/bash

# Usage: ./post.sh <token> <username> <message>

token=$1
username=$2
message=$3

payload='{"userName":"'$username'","text":"'$message'"}'

curl -v \
  -H "Content-Type:application/json" \
  -H "authorization:${token}" \
  --request POST \
  --data ${payload} \
  http://localhost:3000/api/messages
