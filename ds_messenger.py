# ds_messenger.py

# Junyu Li
# junyul24@uci.edu
# junyul031030@gmail.com
# 86676906
"""A module of ds_messenger.py"""
import socket
import time
import json
from collections import namedtuple
DataTuple = namedtuple('DataTuple',
                       ['response', 'type', 'message', 'token', 'messages'])


class DirectMessage:
    """Directmessage"""
    def __init__(self):
        """Init for directmessage."""
        self.recipient = None
        self.message = None
        self.timestamp = None

    def join_action(self, name, pwd):
        """Process join action and return an information."""
        dic = {"join": {"username": name, "password": pwd, "token": ""}}
        str1 = json.dumps(dic)
        return str1

    def send_direct_message(self, usertoken, entry, username):
        """Send direct message to a user."""
        self.timestamp = time.time()
        dic = {"token": usertoken,
               "directmessage": {"entry": entry,
                                 "recipient": username,
                                 "timestamp": self.timestamp}}
        str1 = json.dumps(dic)
        return str1

    def request_unread_messages(self, usertoken):
        """Request new messages."""
        dic = {"token": usertoken, "directmessage": "new"}
        str1 = json.dumps(dic)
        return str1

    def request_all_messages(self, usertoken):
        """Request all messages."""
        dic = {"token": usertoken, "directmessage": "all"}
        str1 = json.dumps(dic)
        return str1

    def extract_json(self, json_msg: str) -> DataTuple:
        """Call the json_loads function"""
        try:
            json_obj = json.loads(json_msg)
            response = json_obj['response']
            type = json_obj['response']['type']
            if 'message' in json_obj['response']:
                message = json_obj['response']['message']
            else:
                message = None
            if 'token' in json_obj['response']:
                token = json_obj['response']['token']
            else:
                token = None
            if 'messages' in json_obj['response']:
                messages = json_obj['response']['messages']
            else:
                messages = None
        except json.JSONDecodeError:
            print("Json cannot be decoded.")
        else:
            return DataTuple(response, type, message, token, messages)


class DirectMessenger:
    """Directmessenger."""
    def __init__(self, dsuserver=None, username=None, password=None):
        """init for directmessenger."""
        self.token = None
        self.dsuserver = dsuserver
        self.username = username
        self.password = password

    def send(self, message: str, recipient: str) -> bool:
        """return true and false."""
        # must return true if message successfully sent, false if send failed.
        message_obj = DirectMessage()
        message_obj.message = message
        message_obj.recipient = recipient
        self.get_token()
        send_message = message_obj.send_direct_message(
            self.token, message_obj.message, message_obj.recipient)
        return self.sending_message(send_message)

    def retrieve_new(self) -> list:
        """retrieve new and return list."""
        # must return a list of DirectMessage objects
        # containing all new messages
        mess_obj = DirectMessage()
        self.get_token()
        new_message = mess_obj.request_unread_messages(self.token)
        receive = self.request_message(new_message)
        return receive

    def retrieve_all(self) -> list:
        """retrieve all and return list."""
        # must return a list of DirectMessage objects containing all messages
        mess_obj = DirectMessage()
        self.get_token()
        all_message = mess_obj.request_all_messages(self.token)
        receive = self.request_message(all_message)
        return receive

    def sending_message(self, command):
        """sending message to people."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bioserver:
            bioserver.connect((self.dsuserver, 3021))
            send = bioserver.makefile('w')
            receive = bioserver.makefile('r')
            send_message = command
            send.write(send_message + '\r\n')
            send.flush()
            join_message = receive.readline()
            mess_obj = DirectMessage()
            response = mess_obj.extract_json(join_message).type
            if response != 'ok':
                return False
            else:
                return True

    def request_message(self, command):
        """request message."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bioserver:
            bioserver.connect((self.dsuserver, 3021))
            send = bioserver.makefile('w')
            receive = bioserver.makefile('r')
            send_message = command
            send.write(send_message + '\r\n')
            send.flush()
            join_message = receive.readline()
            mess_obj = DirectMessage()
            response = mess_obj.extract_json(join_message).type
            if response != 'ok':
                return False
            else:
                message_lis = mess_obj.extract_json(join_message).messages
                new_lis = []
                for item in message_lis:
                    obj = DirectMessage()
                    obj.message = item["message"]
                    obj.recipient = item["from"]
                    obj.timestamp = item["timestamp"]
                    new_lis.append(obj)
                return new_lis

    def get_token(self):
        """get token."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021))
            send = client.makefile('w')
            receive = client.makefile('r')
            mes_obj = DirectMessage()
            join_message = mes_obj.join_action(self.username, self.password)
            send.write(join_message + '\r\n')
            send.flush()
            join_message = receive.readline()
            response = mes_obj.extract_json(join_message).type
            if response != 'ok':
                return False
            else:
                self.token = mes_obj.extract_json(join_message).token
