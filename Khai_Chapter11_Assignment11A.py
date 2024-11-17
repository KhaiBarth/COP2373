# In this assignment, I am creating a program to simulate a poker game. The user is shown a deck of cards, and then enters a number to quantify how many cards they want to change.


import random

# Define a Card class to represent individual cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define a class to represent a complete deck
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Deck.suits for rank in Deck.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num):
        dealt_cards = []
        for _ in range(num):
            if self.cards:
                dealt_cards.append(self.cards.pop())
        return dealt_cards

# This shows the user their "Current hand" (what cards they have)
def display_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card}")

def main():
    # Create and shuffle the deck
    deck = Deck()

    # Deal an initial Poker hand of 5 cards
    hand = deck.deal(5)
    print("Your hand of cards:")
    display_hand(hand)

    # Ask the user which cards to replace
    replace_indices = input("Enter the numbers of the cards you want to replace (Type a number through 1-5), or press Enter to keep all: ").split(',')

    # Validate and process and produce new card set
    if replace_indices != ['']:
        replace_indices = [int(i) - 1 for i in replace_indices if i.isdigit() and 1 <= int(i) <= 5]
        for index in replace_indices:
            hand[index] = deck.deal(1)[0]

    print("\nYour new hand:")
    display_hand(hand)

if __name__ == "__main__":
    main()
