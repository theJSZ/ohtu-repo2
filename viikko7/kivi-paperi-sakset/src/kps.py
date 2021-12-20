from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu

class KPS:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto()

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ekan_siirto = None):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class KpsTekoaly(KPS):
    def __init__(self):
        self._siirto = 0

    def _toisen_siirto(self, ekan_siirto=None):
        self._siirto = (self._siirto + 1) % 3
        siirrot = ["k", "p", "s"]
        print(f'Tietokone valitsi: {siirrot[self._siirto]}')
        return siirrot[self._siirto]

class KpsParempiTekoaly(KPS):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto=None):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)

        return tokan_siirto

class KpsPelaajaVsPelaaja(KPS):
    def _toisen_siirto(self, ekan_siirto=None):
        return input("Toisen pelaajan siirto: ")
        