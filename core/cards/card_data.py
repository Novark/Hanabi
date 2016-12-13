"""
Data
"""

from utilities.types import Enum

_suits = Enum(
    "RED",
    "BLUE",
    "GREEN",
    "YELLOW",
    "WHITE"
)

_faces = Enum(
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE"
)

suits = [
    _suits.RED,
    _suits.BLUE,
    _suits.GREEN,
    _suits.YELLOW,
    _suits.WHITE
]

faces = [
    _faces.ONE,
    _faces.TWO,
    _faces.THREE,
    _faces.FOUR,
    _faces.FIVE
]

cards = []
for suit in suits:
    #Add ONE x3
    for _ in range(0, 3):
        cards.append({
            "suit": suit,
            "face": _faces.ONE
        })

    #Add TWO x2
    for _ in range(0, 2):
        cards.append({
            "suit": suit,
            "face": _faces.TWO
        })

    #Add THREE x2
    for _ in range(0, 2):
        cards.append({
            "suit": suit,
            "face": _faces.THREE
        })

    #Add FOUR x2
    for _ in range(0, 2):
        cards.append({
            "suit": suit,
            "face": _faces.FOUR
        })

    #Add FIVE x1
    for _ in range(0, 1):
        cards.append({
            "suit": suit,
            "face": _faces.FIVE
        })
