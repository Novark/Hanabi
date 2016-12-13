"""
Launches the game client
"""

from core import hanabi_client as hc
from network import client

#Server Settings
ADDRESS = "localhost"
PORT = 54329

#Client Settings
PLAYER_NAME = "Turd Ferguson"


def connect(address, port, player_name):
    """
    Creates the client socket and connect to the game server
    @return: None
    """

    _client = client.Client(address, port)

    print "Launching Hanabi Game Client..."
    game_client = hc.GameClient(_client, player_name)
    game_client.Run()

    print "Terminating Hanabi Game Client..."


if __name__ == "__main__":

    #Run
    connect(ADDRESS, PORT, PLAYER_NAME)
