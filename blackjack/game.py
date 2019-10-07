from .player import Player
from .deck import Deck

class Game():

    def __init__(self, player_name, chip_total):
        self.dealer = Player('Dealer', -1)
        self.player = Player(player_name, chip_total)
        self.deck = Deck()

    def play_round(self):
        self.dealer.reset()
        self.player.reset()
        self.deck.reset()
        print("Lets get started!")

        # prompt player for wager
        while True:
            print('You currently have ' + str(self.player.chips) + ' chips.')
            wager = input("How much do you want to bet [Enter an integer]? ")
            if wager.isdigit():
                wager = int(wager)
                if wager <= self.player.chips:
                    print()
                    break
                else:
                    print('Please enter a number within your chip holdings. \n')
            else:
                print('Please enter an integer amount. \n')

        
        # deal to dealer and player [deals according to official blackjack ruleset]
        self.player.hit(self.deck.deal())

        # hide dealer's first card
        dealer_first_card = self.deck.deal()
        dealer_first_card.hide()
        self.dealer.hit(dealer_first_card)

        # hit rest in order
        self.player.hit(self.deck.deal())
        self.dealer.hit(self.deck.deal())

        print('Dealing...')
        print("Dealer's hand: " + str(self.dealer.hand) + '\n')
        print("Your hand: " + str(self.player.hand))
        print("Your total: " + str(self.player.points()))
        print()

        if self.player.points() == 21 and self.dealer.points() == 21:
            # double naturals
            print("You both got a Blackjack!")
            print("Its a tie. You take back the wager.\n")

        elif self.player.points() == 21:
            # player natural
            print("You got a Blackjack on the first draw!")
            print("You earned 1.5x the wager amount!\n")
            self.player.earn(int(wager*1.5))

        elif self.dealer.points() == 21:
            # dealer natural
            print("The dealer got Blackjack.")
            print("Pay out the wager of " + str(wager) + " .\n")
            self.player.lose(wager)

        else:

            # give player opportunity to hit
            while True:
                move = input("Do you want to hit[h] or stand[s]? ")
                if move != 'h' and move != 's':
                    print('Please supply the correct options ("h" or "s").')
                else:
                    break

            # keep letting player hit
            while move == 'h':
                self.player.hit(self.deck.deal())

                print('Dealing...')
                print("Dealer's hand: " + str(self.dealer.hand) + '\n')
                print("Your hand: " + str(self.player.hand))
                print("Your total: " + str(self.player.points()))
                print()

                if self.player.points() > 21:
                    break

                # prompt user to hit
                while True:
                    move = input("Do you want to hit[h] or stand[s]? ")
                    if move != 'h' and move != 's':
                        print('Please supply the correct options ("h" or "s").')
                    else:
                        break

            if self.player.points() > 21:
                print("You got busted!")
                print("Pay out the wager of " + str(wager) + " .\n")
                self.player.lose(wager)

            else:
                # let the dealer play
                while self.dealer.points() < 17:
                    print('The dealer hit.')
                    self.dealer.hit(self.deck.deal())

                print('Dealing...')
                print("Dealer's hand: " + str(self.dealer.hand) + '\n')
                print("Your hand: " + str(self.player.hand))
                print("Your total: " + str(self.player.points()))
                print()

                if self.dealer.points() > 21:
                    print("The dealer busted!")
                    print("You win!\n")
                    self.player.earn(int(wager))
                elif self.dealer.points() == self.player.points():
                    print("You have the same hand rank as the dealer.")
                    print("You tied!\n")
                elif self.dealer.points() > self.player.points():
                    print("The dealer has the higher hand.")
                    print("You lose!\n")
                    self.player.lose(int(wager))
                elif self.player.points() > self.dealer.points():
                    print("You have the higher hand.")
                    print("You win!\n")
                    self.player.earn(int(wager*1.5))
