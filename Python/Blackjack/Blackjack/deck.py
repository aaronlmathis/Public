import random
from collections import OrderedDict

class Deck:
    
    def __init__(self, number_of_decks):
        # All the cards in one standard deck
        self.single_deck = OrderedDict({
            '2 of Hearts': ('2', 'Hearts'),
            '3 of Hearts': ('3', 'Hearts'),
            '4 of Hearts': ('4', 'Hearts'),
            '5 of Hearts': ('5', 'Hearts'),
            '6 of Hearts': ('6', 'Hearts'),
            '7 of Hearts': ('7', 'Hearts'),
            '8 of Hearts': ('8', 'Hearts'),
            '9 of Hearts': ('9', 'Hearts'),
            '10 of Hearts': ('10', 'Hearts'),
            'Jack of Hearts': ('Jack', 'Hearts'),
            'Queen of Hearts': ('Queen', 'Hearts'),
            'King of Hearts': ('King', 'Hearts'),
            'Ace of Hearts': ('Ace', 'Hearts'),
            '2 of Diamonds': ('2', 'Diamonds'),
            '3 of Diamonds': ('3', 'Diamonds'),
            '4 of Diamonds': ('4', 'Diamonds'),
            '5 of Diamonds': ('5', 'Diamonds'),
            '6 of Diamonds': ('6', 'Diamonds'),
            '7 of Diamonds': ('7', 'Diamonds'),
            '8 of Diamonds': ('8', 'Diamonds'),
            '9 of Diamonds': ('9', 'Diamonds'),
            '10 of Diamonds': ('10', 'Diamonds'),
            'Jack of Diamonds': ('Jack', 'Diamonds'),
            'Queen of Diamonds': ('Queen', 'Diamonds'),
            'King of Diamonds': ('King', 'Diamonds'),
            'Ace of Diamonds': ('Ace', 'Diamonds'),
            '2 of Clubs': ('2', 'Clubs'),
            '3 of Clubs': ('3', 'Clubs'),
            '4 of Clubs': ('4', 'Clubs'),
            '5 of Clubs': ('5', 'Clubs'),
            '6 of Clubs': ('6', 'Clubs'),
            '7 of Clubs': ('7', 'Clubs'),
            '8 of Clubs': ('8', 'Clubs'),
            '9 of Clubs': ('9', 'Clubs'),
            '10 of Clubs': ('10', 'Clubs'),
            'Jack of Clubs': ('Jack', 'Clubs'),
            'Queen of Clubs': ('Queen', 'Clubs'),
            'King of Clubs': ('King', 'Clubs'),
            'Ace of Clubs': ('Ace', 'Clubs'),
            '2 of Spades': ('2', 'Spades'),
            '3 of Spades': ('3', 'Spades'),
            '4 of Spades': ('4', 'Spades'),
            '5 of Spades': ('5', 'Spades'),
            '6 of Spades': ('6', 'Spades'),
            '7 of Spades': ('7', 'Spades'),
            '8 of Spades': ('8', 'Spades'),
            '9 of Spades': ('9', 'Spades'),
            '10 of Spades': ('10', 'Spades'),
            'Jack of Spades': ('Jack', 'Spades'),
            'Queen of Spades': ('Queen', 'Spades'),
            'King of Spades': ('King', 'Spades'),
            'Ace of Spades': ('Ace', 'Spades')
        })

        # Create the whole deck with the specified number of decks
        self.whole_deck = self.create_deck(number_of_decks)
        # Shuffle the deck initially
        self.shuffle_deck()

    def create_deck(self, number_of_decks):
        whole_deck = []
        # Iterate through the number of decks to be included
        for i in range(number_of_decks):
            # Iterate through the original single_deck
            for card_name, card_value in self.single_deck.items():
                # Create a unique key for each card in each deck
                unique_card_name = f"{card_name} (Deck {i+1})"
                # Add the card to the whole deck
                whole_deck.append((unique_card_name, card_value))
        return whole_deck

    def shuffle_deck(self):
        random.shuffle(self.whole_deck)

    def __str__(self):
        return f"Deck with {len(self.whole_deck)} cards"

    def draw_card(self):
        return self.whole_deck.pop() if self.whole_deck else None

