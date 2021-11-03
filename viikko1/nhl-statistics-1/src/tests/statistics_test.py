import unittest
from statistics import Statistics, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [Player("Semenko", "EDM", 4, 12),
                Player("Lemieux", "PIT", 45, 54),
                Player("Kurri", "EDM", 37, 53),
                Player("Yzerman", "DET", 42, 56),
                Player("Gretzky", "EDM", 35, 89)]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    # def test_sort_by_points(self):
    #     self.assertEqual(sort_by_points(self.statistics.get_players()[0]), 12)

    def test_search_player_present(self):
        player1 = self.statistics.search("Kurri")
        self.assertEqual(player1.name, "Kurri")
        self.assertEqual(player1.team, "EDM")
        self.assertEqual(player1.goals, 37)
        self.assertEqual(player1.assists, 53)

    def test_search_player_not_present(self):
        self.assertEqual(self.statistics.search("Mömmö"), None)

    def test_team_valid(self):
        players = self.statistics.team("EDM")
        for player in players:
            self.assertEqual(player.team, "EDM")

    def test_top_scorers(self):
        top = self.statistics.top_scorers(3)
        for i in range(len(top)-1):
            self.assertGreaterEqual(top[i].points, top[i+1].points)