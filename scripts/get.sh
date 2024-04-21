#!/bin/bash

# Usage: ./get.sh <token>

token=$1

curl -v \
  -H "authorization:${token}" \
  --request GET \
  http://thwopzap.net/api/messages
