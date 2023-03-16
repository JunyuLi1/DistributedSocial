# test_ds_message_protocol.py.py for assignment 5 in ICS 32
# Programming with Software Libraries in Python
# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
import unittest
import socket
import ds_protocol


def simple_client(message, address='168.235.86.101', port=3021):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((address, port))
        send = client.makefile('w')
        receive = client.makefile('r')
        msg = message
        send.write(msg + '\r\n')
        send.flush()
        resp = receive.readline()
        return resp


class TestDSmessenger(unittest.TestCase):
    """Class for testing ds_protocol."""
    def test_send_direct_protocol(self):
        """Test direct_send protocol function."""
        usertoken = '54559cc3-334b-4fd2-ac4d-5dd0462c3f15'
        entry = 'Hi from VC'
        username = 'VC1'
        test_message = ds_protocol.send_direct_message(usertoken, entry, username)
        returned_result = ds_protocol.extract_json(simple_client(test_message)).type
        assert returned_result == 'ok'

    def test_request_new(self):
        """Test request_new protocol function."""
        usertoken = '54559cc3-334b-4fd2-ac4d-5dd0462c3f15'
        test_message = ds_protocol.request_unread_messages(usertoken)
        returned_result = ds_protocol.extract_json(simple_client(test_message)).type
        assert returned_result == 'ok'

    def test_request_all(self):
        """Test request_all protocol function."""
        usertoken = '54559cc3-334b-4fd2-ac4d-5dd0462c3f15'
        test_message = ds_protocol.request_all_messages(usertoken)
        returned_result = ds_protocol.extract_json(simple_client(test_message)).type
        assert returned_result == 'ok'


if __name__ == "__main__":
    unittest.main()
