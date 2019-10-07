# Ayush Jain's KP Fellowship Engineering Challenge
Ayush's Blackjack project for the KP fellowship.

## Prequisites
- Python 3

## Running the Project
    $ git clone https://github.com/ayushajain/KP-Fellowship-Challenge
    $ cd KP-Fellowship-Challenge
    $ python main.py

## Design Process

I chose Python because:
- Its simple and easy to read
- It has substantial internal libraries which make implementing certain tasks much simpler and cleaner
- Its the language I'm most used to right now, its just as optimal for making a simple unix friendly game.

I designed this blackjack game using a top-down design approach. I started by identifying the main components of this game, and decomposing them into smaller parts to ensure modularity.

The main module of this game is the 'Game' class which handles the bulk of the round operations. This is where everything comes together to make the chunk of the blackjack game.

I broke this game down even more by creating a 'Player' class which keeps track of the individual players and dealer. Although this version only has a single player, I designed it to allow for multiple players to be potentially added to the game by abstracting many of the reused methods.

Additionally, I created a 'card' class to keep track of individual cards. I also allowed for each of these cards to be hidden for the case of the dealer and potentially adding more players.

The 'deck' class contains all these cards and uses the internal 'random' python module to shuffle the list of cards.

As reference for values, I kept all globals for the 'blackjack' module within 'reference.py' to ensure uniformity.


