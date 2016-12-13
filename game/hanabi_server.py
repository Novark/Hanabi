"""
Server game logic implementation
"""

import random

from players import player_server as ps
from network import message
from network import protocol

class Rule(object):
    pass

class Round(object):
    #Maybe this is just a property in the Game class...
    pass

class Game(object):
    pass

class GameServer(object):
    """
    Implements the game server logic
    """

    def __init__(self, server, player_count):
        self.server = server
        self.target_player_count = player_count
        self.current_player_count = 0
        self.players = []

    def _wait_add_player(self):
        """
        Wait for a player to connect, and then add them to the server
        @return: A player object
        """

        socket, data_tuple = self.server.accept()
        return self._add_player(socket, data_tuple[0], data_tuple[1])

    def _add_player(self, socket, address, port):
        """
        Adds a new player to the server
        @param socket: The socket used to communicate with this player
        @param address: The player's network address
        @param port: The player's network port
        @return: A player object
        """

        print "ADDING PLAYER TO SERVER: %s:%s" % (address, port)
        player = ps.Player(socket, address, port)

        #TODO: Set player name after the fact maybe (self._set_player_name ... or ... self._set_player_data(name))

        self.players.append(player)
        self.current_player_count += 1 #TODO: Need to handle players disconnecting

        return player

    def _receive_message_player(self, player):
        """
        Waits for a message from the specified player
        @param player: The player to receive the message from
        @return: A Message object; None if an error occurred
        """

        return self.server.receive_message(player.socket)

    def _send_message_all_players(self, players, msg):
        """
        Sends a message to all players
        @param players: A list of players
        @param msg: A Message object
        @return: None
        """

        if len(players) == 0:
            print("WARNING: No players to send to; no action required")
            return None

        sockets = [player.socket for player in players]
        return self.server.send_message_all_clients(sockets, msg)

    def _send_message_player(self, player, msg):
        """
        Sends a message to the specified player
        @param player: The player to send the message to
        @param msg: A Message object
        @return: None
        """

        return self.server.send_message(player.socket, msg)

    def Run(self):
        self.server.run()

        while self.current_player_count < self.target_player_count:
            player = self._wait_add_player()
            print "SERVER: Waiting for player data..."

            msg = self._receive_message_player(player)
            print "SERVER: Got message from player: %s" % str(msg.json)

        print "All players connected!  Starting Game..." #TODO: DEBUG
        #TODO: The rest of the game logic...

        msg = message.Message(
            protocol.generic_msg_types.GOODBYE,
            {}
        )
        self._send_message_all_players(self.players, msg) #TODO: DEBUG


