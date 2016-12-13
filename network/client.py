"""
Hanabi Client
"""

import socket

import socket_json as sj
import message


class Client(object):
    """
    Client class
    """

    def __init__(self, address, port):
        self.server_address = address
        self.server_port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connects the client to the server
        @return: None
        """

        self.socket.connect(
            (self.server_address, self.server_port)
        )

    def send_message(self, msg):
        """
        Sends a message to the server
        @param msg: A Message object
        @return: None
        """

        try:
            sj.send_json(self.socket, msg.json)
        except Exception, e:
            print "ERROR: Client could not send data; %s" % str(e)

        return None

    def receive_message(self):
        """
        Waits for a message from the server
        @return: A Message object; None if an error occurred
        """

        try:
            json = sj.receive_json(self.socket)
            if "type" not in json:
                print "ERROR: Unable to receive message from the server, no message type"
                return None

            if "data" not in json:
                print "ERROR: Unable to receive message from the server, no message data"
                return None

            msg = message.Message(json["type"], json["data"])
            return msg
        except Exception, e:
            print "ERROR: Client could not receive data; %s" % str(e)

        return None

    def __del__(self):
        """
        Close the socket connection
        @return: None
        """

        self.socket.close()
        self.socket = None

