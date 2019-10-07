from blackjack.game import Game


def run():
    # start first game
    print("Welcome to Black Jack!")

    # prompt user for name and chips
    name = input("Enter your name: ")
    while True:
        chip_total = input("Enter how many chips you have [Enter an integer]: ")
        if chip_total.isdigit():
            chip_total = int(chip_total)
            print()
            break
        else:
            print('Please enter an integer amount. \n')
            
    # initialize game
    game = Game(name, chip_total)
    game.play_round()

    while input("Would you like to play another round? Type 'y' to play another round, or any other character to stop. ") == 'y':
        game.play_round()

    print('\nThanks for playing Black Jack!')


if __name__ == '__main__':
    run()