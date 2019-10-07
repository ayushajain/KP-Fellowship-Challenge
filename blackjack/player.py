from .reference import *

class Player():

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []

    def points(self):
        total = 0
        num_aces = 0

        # sum up card rank values
        for card in self.hand:
            if card.rank == 'Ace':
                num_aces +=1
            total += values[card.rank]

        # subtract ace values to reach below 21
        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1

        return total

    def earn(self, amount):
        self.chips += amount

    def lose(self, amount):
        self.chips -= amount

    def hit(self, card):
        self.hand.append(card)

    def reset(self):
        self.hand = []


    