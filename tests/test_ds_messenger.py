# test_ds_messenger.py

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module for testing ds_messenger.py"""
import unittest
import json
import socket
import ds_messenger


def simple_client(message, address='168.235.86.101', port=3021):
    """simple client function."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((address, port))
        send = client.makefile('w')
        receive = client.makefile('r')
        msg = message
        send.write(msg + '\r\n')
        send.flush()
        resp = receive.readline()
        return resp


def is_json(data):
    """test json format."""
    try:
        json.loads(data)
        return True
    except ValueError:
        return False


class TestDSmessenger(unittest.TestCase):
    """Class for testing ds_messenger."""
    def test_direct_send(self):
        """Test direct send function."""
        message_to_send = 'Hi, I\'m 10'
        recipient = 'VC1'
        user = ds_messenger.DirectMessenger('168.235.86.101',
                                            'nicaiwoshishei', 'buxiangshuohua')
        returned_result = user.send(message_to_send, recipient)
        assert returned_result is True
        user = ds_messenger.DirectMessenger(
            '168.235.86.101', 'nicaiwoshishei', 'buxiangshuohua222')
        returned_result = user.send(message_to_send, recipient)
        assert returned_result is False

    def test_request_new(self):
        """Test request_new function."""
        user = ds_messenger.DirectMessenger('168.235.86.101', 'VC1', 'VC')
        returned_result = user.retrieve_new()
        assert isinstance(returned_result, list)
        assert isinstance(returned_result[0], ds_messenger.DirectMessage)

    def test_request_all(self):
        """Test request_new function."""
        user = ds_messenger.DirectMessenger('168.235.86.101', 'VC1', 'VC')
        returned_result = user.retrieve_all()
        assert isinstance(returned_result, list)
        assert isinstance(returned_result[0], ds_messenger.DirectMessage)

    def test_join_action(self):
        """Test join action."""
        obj = ds_messenger.DirectMessage()
        result = obj.join_action('VC1', 'VC')
        assert is_json(result)

    def test_extract_json(self):
        """Test extract json."""
        message = '{"response": ' \
                  '{"type": "ok", "message": ' \
                  '"Welcome back, math3a", "token": ' \
                  '"9f360cbd-aea0-438b-bb04-122600409581"}}'
        result = ds_messenger.DirectMessage().extract_json(message)
        assert isinstance(result, tuple)

    def test_request_new_new(self):
        """Test request_new protocol function."""
        usertoken = '6e79a5fd-2b96-4c48-8ae5-938c8dbb0e54'
        entry = 'Hi from 10'
        username = 'VC1'
        obj = ds_messenger.DirectMessage()
        test_message = obj.send_direct_message(
            usertoken, entry, username)
        returned_result = \
            obj.extract_json(simple_client(test_message)).type
        assert returned_result == 'ok'


if __name__ == "__main__":
    unittest.main()
