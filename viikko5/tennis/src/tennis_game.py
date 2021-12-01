class TennisGame:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_strings = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_tie_string(self):
        if self.player1_score > 3:
            return "Deuce"
        return f'{self.score_strings[self.player1_score]}-All'

    def tie(self):
        return self.player1_score == self.player2_score

    def both_over_30(self):
        return self.player1_score >= 3 and self.player2_score >= 3

    def get_normal_score_string(self):
        return f'{self.score_strings[self.player1_score]}-{self.score_strings[self.player2_score]}'

    def get_leader(self):
        if self.player1_score > self.player2_score:
            return "player1"
        if self.player2_score > self.player1_score:
            return "player2"

    def get_winner(self):
        winner = None
        if max(self.player1_score, self.player2_score) > 3 and abs(self.player1_score - self.player2_score) > 1:
            if self.player1_score > self.player2_score:
                winner = "player1"
            else:
                winner = "player2"
        return winner

    def get_score(self):
        if self.get_winner():
            return f'Win for {self.get_winner()}' 

        if self.tie():
            return self.get_tie_string()

        if not self.both_over_30():
            return self.get_normal_score_string()

        return f'Advantage {self.get_leader()}'
