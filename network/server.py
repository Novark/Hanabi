"""
Hanabi Server
"""

import socket

import socket_json as sj
import message


#TODO: Probably want to keep this as network-only, and not use "Players"..."Clients" only
#TODO: Interface for this class would exist in hanabi_server, and would call into here...see TODOs below
#TODO: Ditto for client.py, although this seems to already be OK I think

class Server(object):
    """
    Server class
    """

    #Maximum number of queued connections
    backlog = 5

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        """
        Performs the server setup and starts listening for connections
        @return: None
        """

        self.socket.bind(
            (self.address, self.port)
        )

        self.socket.listen(self.backlog)


    def accept(self):
        """
        Waits for a client to connect
        @return: A tuple containing a socket and address
        """

        return self.socket.accept()

    def send_message(self, socket, msg):
        """
        Sends a message to a client through the specified socket
        @param socket: The socket to send to
        @param msg: A Message object
        @return: None
        """

        print "SENDING MESSAGE TO CLIENT: TYPE=%s; DATA=%s" % (msg.type, msg.data) #DEBUG

        try:
            sj.send_json(socket, msg.json)
        except Exception, e:
            print "ERROR: Server could not send data to client; %s" % str(e)

        return None

    def send_message_all_clients(self, sockets, msg):
        """
        Sends a message to all clients through the specified sockets
        @param sockets: A list of client sockets
        @param msg: A Message object
        @return: None
        """

        #TODO: This gets moved to hanabi_server most likely

        #TODO: May want to have a TX / RX context here that tracks ACKs and re-sending of data so that clients don't fall out of sync
        #TODO: Context may need to be held by the GameServer in order to wait before ending the round or doing whatever needs to be done

        try:
            for socket in sockets:
                self.send_message(socket, msg)
        except Exception, e:
            print "ERROR: Server could not send data to player; %s" % str(e)

        return None

    def receive_message(self, socket):
        """
        Waits for a message from the specified client socket
        @socket: The client socket to listen on
        @return: A Message object; None if an error occurred
        """

        #TODO: This probably needs to become threaded (unless the game model is truely turn based, and only the curent player can send...basically fully atomic)

        try:
            json = sj.receive_json(socket)
            if "type" not in json:
                print "ERROR: Unable to receive message from the client, no message type"
                return None

            if "data" not in json:
                print "ERROR: Unable to receive message from the client, no message data"
                return None

            msg = message.Message(json["type"], json["data"])
            return msg
        except Exception, e:
            print "ERROR: Server could not receive message from player; %s" % str(e)

        return None

    def __del__(self):
        """
        Close the socket connection
        @return: None
        """

        #TODO: Notify clients?  for client in clients:  client.close() ?
        self.socket.close()
        self.socket = None

