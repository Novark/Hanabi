"""
Launches the game server
"""

from core import hanabi_server as hs
from network import server

#Server Settings
ADDRESS = "localhost"
PORT = 54329


def start_server(address, port):
    """
    Creates the server socket and launches the game server
    @return: None
    """

    _server = server.Server(address, port)

    print "Launching Hanabi Game Server..."
    game_server = hs.GameServer(_server)
    game_server.Run()

    print "Terminating Hanabi Game Server..."


if __name__ == "__main__":

    #Run
    start_server(ADDRESS, PORT)
