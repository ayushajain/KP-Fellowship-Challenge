import random
from .card import Card
from .reference import *


class Deck():

    def __init__(self):
        self.deck = []

        # initialize deck of 52 cards
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.deck = []
        # initialize deck of 52 cards
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

        self.shuffle()

    def get(self):
        return self.deck

    def deal(self):
        return self.deck.pop()