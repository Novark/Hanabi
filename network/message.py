"""
Message implementation
"""

class Message(object):
    """
    This defines the structure in which the server and clients are expected to communicate
    """

    def __init__(self, message_type, message_data):
        self.type = message_type
        self.data = message_data
        self.json = {
            "type": self.type,
            "data": self.data
        }
