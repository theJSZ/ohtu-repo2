import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_maara_oikein_yhden_tuotteen_jalkeen(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # step 3
    def test_hinta_oikein_yhden_tuotteen_jalkeen(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.hinta(), 2)

    # step 4
    def test_kahden_tuotteen_jalkeen_maara_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 5
    def test_kahden_eri_tuotteen_jalkeen_hinta_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("leipä", 3))
        self.assertEqual(self.kori.hinta(), 5)

    # step 6
    def test_kahden_eri_tuotteen_jalkeen_maara_oikein(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("leipä", 2))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7
    def test_kahden_saman_tuotteen_jalkeen_hinta_oikein(self):
        tuote = Tuote("maito", 2)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(), 4)

    # step 8
    def test_yhden_tuotteen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
 
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    # step 10
    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(Tuote("maito", 2))
        self.kori.lisaa_tuote(Tuote("leipä", 3))
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    # step 11
    def test_kahden_saman_tuotteen_jalkeen_korissa_yksi_ostos(self):
        maito = Tuote("maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    # step 12
    def test_kahden_saman_tuotteen_jalkeen_korissa_oikeanlainen_ostos(self):
        maito = Tuote("maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "maito")
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)

    # step 13
    def test_kahdesta_samanlaisesta_tuotteesta_yhden_poistaminen_jattaa_yhden_jaljelle(self):
        maito = Tuote("maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)

    # step 14
    def test_korista_ainoan_tuotteen_poistaminen_jattaa_tyhjan_korin(self):
        maito = Tuote("maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.hinta(), 0)
    
    # step 15
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("maito", 2)
        leipa = Tuote("leipä", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()), 0)
        self.assertEqual(self.kori.hinta(), 0)
    
        
