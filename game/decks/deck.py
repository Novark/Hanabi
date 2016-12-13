"""
Deck implementation
"""

import random

from game.cards import card
from game.cards import card_data

class Deck(object):

    def __init__(self):
        self.cards = []
        self.setup()

    def setup(self):
        """
        Sets up the deck.  By default, this involves populating the deck with cards, and then performing a shuffle
        @return: None
        """

        for c in card_data.cards:
            self.cards.append(card.Card(c["suit"], c["face"]))

        self.shuffle()

    def shuffle(self):
        """
        Shuffles the deck
        @return: None
        """

        random.shuffle(self.cards)

    def take_card(self):
        """
        Takes a card from the top of the deck
        @return: A card if successful; None if the deck is empty
        """

        if self.deck_is_empty():
            return None
        else:
            return self.cards.pop(0)

    def deck_is_empty(self):
        """
        Indicates whether the deck is empty
        @return: True if the deck is empty; False otherwise
        """

        return len(self.cards) > 0