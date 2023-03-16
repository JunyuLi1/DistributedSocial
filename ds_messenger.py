# Starter code for assignment 5 in ICS 32
# Programming with Software Libraries in Python
# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
import socket
import ds_protocol


class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((dsuserver, 3021))
            send = client.makefile('w')
            receive = client.makefile('r')
            msg = ds_protocol.join_action(username, password)
            send.write(msg + '\r\n')
            send.flush()
            resp = receive.readline()
            returned_token = ds_protocol.extract_json(resp).token
        self.token = returned_token
        self.dsuserver = dsuserver
        self.username = username
        self.password = password

    def send(self, message: str, recipient: str) -> bool:
        # must return true if message successfully sent, false if send failed.
        send_message = ds_protocol.send_direct_message(self.token, message, recipient)
        return self.sending_message(send_message)

    def retrieve_new(self) -> list:
        # must return a list of DirectMessage objects containing all new messages
        new_message = ds_protocol.request_unread_messages(self.token)
        receive = self.request_message(new_message)
        return receive

    def retrieve_all(self) -> list:
        # must return a list of DirectMessage objects containing all messages
        all_message = ds_protocol.request_all_messages(self.token)
        receive = self.request_message(all_message)
        return receive

    def sending_message(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bioserver:
            bioserver.connect((self.dsuserver, 3021))
            send = bioserver.makefile('w')
            receive = bioserver.makefile('r')
            send_message = command
            send.write(send_message + '\r\n')
            send.flush()
            join_message = receive.readline()
            response = ds_protocol.extract_json(join_message).type
            if response != 'ok':
                return False
            else:
                return True

    def request_message(self, command):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bioserver:
            bioserver.connect((self.dsuserver, 3021))
            send = bioserver.makefile('w')
            receive = bioserver.makefile('r')
            send_message = command
            send.write(send_message + '\r\n')
            send.flush()
            join_message = receive.readline()
            response = ds_protocol.extract_json(join_message).type
            if response != 'ok':
                return False
            else:
                return ds_protocol.extract_json(join_message).messages
