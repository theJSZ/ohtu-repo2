class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        return [str(player) for player in sorted(self.reader.get_players()) if player.nationality == nationality]