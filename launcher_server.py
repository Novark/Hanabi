"""
Launches the game server
"""

from game import hanabi_server as hs
from network import server

#Server Settings
ADDRESS = "localhost"
PORT = 54329
PLAYER_COUNT = 2


def start_server(address, port, player_count):
    """
    Creates the server socket and launches the game server
    @return: None
    """

    _server = server.Server(address, port)

    print "Launching Hanabi Game Server..."
    game_server = hs.GameServer(_server, player_count)
    game_server.Run()

    print "Terminating Hanabi Game Server..."


if __name__ == "__main__":

    #Run
    start_server(ADDRESS, PORT, PLAYER_COUNT)
