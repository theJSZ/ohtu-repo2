import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    def test_tavaroiden_maara_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_hinta_oikein_yhden_tuotteen_jalkeen(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_tuotteen_jalkeen_maara_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_jalkeen_hinta_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("leipä", 3))
        self.assertEqual(self.kori.hinta(), 5)

