"""
Client game logic implementation
"""

from network import message
from network import protocol

class GameClient(object):
    """
    Implements the game client logic
    """

    def __init__(self, client, player_name):
        self.client = client
        self.player_name = player_name

    def Run(self):
        try:
            self.client.connect()
        except Exception, e:
            print "ERROR: Unable to connect to server"
            return None

        msg_tx = message.Message(
            protocol.generic_msg_types.PROVIDE_DATA,
            {"player_name": self.player_name}
        )
        self.client.send_message(msg_tx)

        while True:
            msg_rx = self.client.receive_message()
            if msg_rx:
                print "MESSAGE RECEIVED FROM SERVER: TYPE=%s; DATA=%s" % (msg_rx.type, msg_rx.data) #DEBUG: My stuff

