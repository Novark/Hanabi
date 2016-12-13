"""
Hanabi network protocol definition
"""

from utilities.types import Enum

#TODO: Define the various types of messages and data that can be sent to / from the server / client


#GENERIC MESSAGE TYPES
generic_msg_types = Enum(
    "HELLO",
    "GOODBYE",

    "ACK",
    "NAK",

    "REQUEST_DATA",
    "PROVIDE_DATA"
)

#SERVER MESSAGE TYPES
server_msg_types = Enum(
    "WHO_ARE_YOU",
)

#CLIENT MESSAGE TYPES
client_msg_types = Enum(
    "I_AM"
)

