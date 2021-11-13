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
        return f"{self.name} -- team: {self.team} -- goals: {self.goals} assists: {self.assists}"
