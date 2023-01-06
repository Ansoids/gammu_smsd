#!/usr/bin/env python3

import os
import sys
import requests

numparts = int(os.environ["DECODED_PARTS"])

text = ""
# Are there any decoded parts?
if numparts == 0:
    text = os.environ["SMS_1_TEXT"]
# Get all text parts
else:
    for i in range(1, numparts + 1):
        varname = "DECODED_%d_TEXT" % i
        if varname in os.environ:
            text = text + os.environ[varname]

# Set the webhook URL and the data to be sent
webhook_url = ""
message = text
string = "FROM: "
number = os.environ["SMS_1_NUMBER"]

data = {
        "text": string + str(number),
    "attachments": [
        {
            "text": message,
            "color": "#36a64f"
        }
    ]
}

# Send a POST request to the webhook with the data
response = requests.post(webhook_url, json=data)
