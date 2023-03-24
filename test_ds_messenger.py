# test_ds_messenger.py for assignment 5 in ICS 32
# Programming with Software Libraries in Python
# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module for testing ds_messenger.py"""
import unittest
import ds_messenger


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


if __name__ == "__main__":
    unittest.main()
