# e.g. using curl
# curl -v -X GET http://thwopzap.net/api/messages \
    #  -H "Authorization: Bearer secret123"

def get_messages_from_api():
    import requests
    import json

    url = "http://thwopzap.net/api/messages"

