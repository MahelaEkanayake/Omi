from player import Player
from dealer import Dealer
from team import Team
import random


class Game:
    def __init__(self):
        self.players = []
        self.dealer = Dealer()
        self.game_number = 0
        self.trump_chooser = None
        self.trump_suit = None
        self.teams = []
        self.current_suit = None
        self.current_turn = None

    def create_players(self):
        self.players = [
            Player("Player 1"),
            Player("Player 2"),
            Player("Player 3"),
            Player("Player 4")
        ]

    def create_teams(self):
        self.teams = [
            Team("Team 1"),
            Team("Team 2")
        ]

        random.shuffle(self.players)

        for i in range(len(self.players)):
            self.teams[i%2].add_player(self.players[i])


    def start(self):
        print("Omi game started!")

        self.create_players()
        self.create_teams()

        print("\nPlayers:")
        for team in self.teams:
            for player in team.players:
                print(f"{player.name} is in {team.name}.")

        print("\n")

        # Create and shuffle deck
        self.dealer.create_deck()
        self.dealer.shuffle()

        # Choose trump player
        if self.trump_chooser is None:
            self.trump_chooser = random.randint(0, 3)
        else:
            self.trump_chooser += 1

            if self.trump_chooser >= 4:
                self.trump_chooser = 0

        self.current_turn = self.trump_chooser

        # Reset trump-player flags
        for player in self.players:
            player.is_trump_chooser = False

        self.players[self.trump_chooser].is_trump_chooser = True

        self.game_number += 1

        # Deal 4 cards to each player
        for i in range(4):
            card_receiver = (i + self.trump_chooser) % 4

            for j in range(4):
                card = self.dealer.deck.pop()
                self.players[card_receiver].receive_card(card)

        self.trump_suit = self.players[self.trump_chooser].select_trump()

        if self.trump_suit == "Open the 7th Card":
            print("Wants to open the 7th card!")
        else:
            print(f"{self.trump_suit} is the trump suit.")

        # Deal the remaining 4 cards to each player
        for i in range(4):
            card_receiver = (i + self.trump_chooser) % 4
        
            for j in range(4):
                card = self.dealer.deck.pop()
                self.players[card_receiver].receive_card(card)

        if self.trump_suit == "Open the 7th Card":
            opened_card = self.players[self.trump_chooser].select_trump_on_7th_card()
            print(f"{self.players[self.trump_chooser].name} opened the {opened_card.rank} of {opened_card.suit} as the 7th card.")
            self.trump_suit = opened_card.suit
            print(f"{self.trump_suit} is the trump suit.")