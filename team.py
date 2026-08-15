class Team:
    def __init__(self, name):
        self.name = name
        self.players = [None] * 2
        self.hands_won = 0
        self.tokens_won = 0

    def add_player(self, player):
        for i in range(2):
            if self.players[i] == None:
                self.players[i] = player
                return