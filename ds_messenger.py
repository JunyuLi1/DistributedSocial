# Starter code for assignment 5 in ICS 32
# Programming with Software Libraries in Python
# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None

    def send(self, message: str, recipient: str) -> bool:
        # must return true if message successfully sent, false if send failed.
        pass

    def retrieve_new(self) -> list:
        # must return a list of DirectMessage objects containing all new messages
        pass

    def retrieve_all(self) -> list:
        # must return a list of DirectMessage objects containing all messages
        pass