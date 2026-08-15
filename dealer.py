import random
from card import Card

class Dealer:
    def __init__(self):
        self.deck = [None] * 32

    def create_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in suits:
            for rank in ranks:
                for i in range(32):
                    if self.deck[i] == None:
                        self.deck[i] = Card(suit, rank)
                        break

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()