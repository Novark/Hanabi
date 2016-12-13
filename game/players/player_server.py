"""
Player implementation (server side)
"""

class Player(object):
    """
    Player Class
    """

    def __init__(self, socket, address, port):
        self.socket = socket
        self.address = address
        self.port = port
        self.player_name = "Player"
        self.hand = []


