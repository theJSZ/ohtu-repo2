class Player:
    def __init__(self, d: dict):
        self.name        = d['name']
        self.nationality = d['nationality']
        self.assists     = d['assists']
        self.goals       = d['goals']
        self.penalties   = d['penalties']
        self.team        = d['team']
        self.games       = d['games']
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:2} + {self.assists:<2} = {self.goals+self.assists}"

    def __gt__(self, other):
        return self.goals + self.assists < other.goals + other.assists
