#!/bin/bash

# Usage: ./get.sh <token>

token=$1

curl -v \
  -H "authorization:${token}" \
  --request GET \
  http://localhost:3000/api/messages
