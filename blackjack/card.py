class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.hidden = False

    def __str__(self):
        # Hide dealer cards
        if self.hidden:
            return '[Hidden]'
        return '[' + self.rank + " of " + self.suit + ']'

    def hide(self):
        self.hidden = True

    def __repr__(self):
        return self.__str__()

