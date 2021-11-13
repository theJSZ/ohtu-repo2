import requests
from player import Player
from datetime import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print(f"Players from FIN {datetime.now()}")

    for player in sorted(players):
        if player.nationality == 'FIN':
            print(player)

main()