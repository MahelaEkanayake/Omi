from card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [None] * 8
        self.trump_suit = None
        self.cards_in_the_hand = 0
        self.is_trump_chooser = False


    def receive_card(self, card):
        for i in range(8):
            if self.hand[i] is None:
                self.hand[i] = card
                self.cards_in_the_hand += 1
                return

    def select_trump(self):

        self.trump_suit = None

        initial_hand_count_per_suit = {
            "Hearts" : 0,
            "Spades" : 0,
            "Diamonds" : 0,
            "Clubs" : 0
        }

        initial_hand_total_value_per_suit = {
            "Hearts" : 0,
            "Spades" : 0,
            "Diamonds" : 0,
            "Clubs" : 0
        }

        initial_hand_has_an_ace = {
            "Hearts" : False,
            "Spades" : False,
            "Diamonds" : False,
            "Clubs" : False
        }

        for i in range(4):

            initial_hand_count_per_suit[self.hand[i].suit] += 1
            initial_hand_total_value_per_suit[self.hand[i].suit] += self.hand[i].value
            initial_hand_has_an_ace[self.hand[i].suit] = True if self.hand[i].rank == "Ace" else False

        max_initial_hand_suit_by_count = max(initial_hand_count_per_suit, key=initial_hand_count_per_suit.get)

        max_initial_hand_suit_by_value = max(initial_hand_total_value_per_suit, key=initial_hand_total_value_per_suit.get)

        max_initial_hand_count_per_suit = max(initial_hand_count_per_suit.values())
            
        if max_initial_hand_count_per_suit>=3:
            self.trump_suit = max_initial_hand_suit_by_count

        if max_initial_hand_count_per_suit==2:
            if 1 in initial_hand_count_per_suit.values():
                self.trump_suit = max_initial_hand_suit_by_count
            else:
                for suit,count in sorted(initial_hand_count_per_suit.items(), key=lambda x: x[1], reverse=True):
                    if count == 2:
                        if initial_hand_has_an_ace[suit]:
                            continue
                        elif suit == max_initial_hand_suit_by_count:
                            self.trump_suit = suit
                            break
                else:
                    self.trump_suit = max_initial_hand_suit_by_value

        if max_initial_hand_count_per_suit == 1:
            self.trump_suit = "Open the 7th Card"

        return self.trump_suit

    def select_trump_on_7th_card(self):
        self.trump_suit = self.hand[6].suit
        return self.hand[6]