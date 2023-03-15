# ds_protocol.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Receive data from DS server and make protocols."""
import json
import time
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['response', 'type', 'message', 'token'])


def extract_json(json_msg: str) -> DataTuple:
    """Call the json.loads function"""
    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        type = json_obj['response']['type']
        message = json_obj['response']['message']
        if 'token' in json_obj['response']:
            token = json_obj['response']['token']
        else:
            token = None
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    else:
        return DataTuple(response, type, message, token)


def join_action(name, pwd):
    """Process join action and return an information."""
    dic = {"join": {"username": name, "password": pwd, "token": ""}}
    str1 = json.dumps(dic)
    return str1


def post_action(usertoken, post):
    """Process post action and return the json format."""
    timestamp = time.time()
    dic = {"token": usertoken, "post": {"entry": post, "timestamp": timestamp}}
    str1 = json.dumps(dic)
    return str1


def bio_action(useertoken, bio):
    """Process with bio action"""
    dic = {"token": useertoken, "bio": {"entry": bio, "timestamp": ""}}
    str1 = json.dumps(dic)
    return str1


def send_direct_message(usertoken, entry, username):
    timestamp = time.time()
    dic = {"token": usertoken, "directmessage": {"entry": entry, "recipient": username, "timestamp": timestamp}}
    str1 = json.dumps(dic)
    return str1


def request_unread_messages(usertoken):
    dic = {"token": usertoken, "directmessage": "new"}
    str1 = json.dumps(dic)
    return str1


def request_all_messages(usertoken):
    dic = {"token": usertoken, "directmessage": "all"}
    str1 = json.dumps(dic)
    return str1
