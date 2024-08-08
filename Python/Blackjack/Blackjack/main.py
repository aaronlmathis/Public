from deck import Deck
from player import Player

def main():
    whole_deck = Deck(2)
    player = Player(500.00, "Aaron")

    print(f"Hello {player.name}. Welcome to the game. You have ${player.bank}")

if __name__ == "__main__":
    main()