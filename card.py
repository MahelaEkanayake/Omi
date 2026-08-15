
class Card:
    def __init__(self, suit, rank):
        self.suit = suit;
        self.rank = rank;

        if self.rank.isdigit():
            self.value = int(rank)
        elif self.rank == "Jack":
            self.value = 11
        elif self.rank == "Queen":
            self.value = 12
        elif self.rank == "King":
            self.value = 13
        elif self.rank == "Ace":
            self.value = 14
        else: self.value = -1