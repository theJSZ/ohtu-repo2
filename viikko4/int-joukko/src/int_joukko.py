KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, lisattava):
        if self.kuuluu(lisattava):
            return False
            
        if self.alkioiden_lkm == len(self.ljono):
            self.ljono.append([0] * self.kasvatuskoko)

        self.ljono[self.alkioiden_lkm] = lisattava
        self.alkioiden_lkm += 1
        return True

    def poista(self, poistettava):
        if not self.kuuluu(poistettava):
            return False

        self.alkioiden_lkm -= 1
        self.ljono.remove(poistettava)
        self.ljono.append(0)
        return True
     
    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [luku for luku in self.ljono[:self.alkioiden_lkm]]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        uusi_joukko = IntJoukko()

        for i in range(joukko1.alkioiden_lkm):
            uusi_joukko.lisaa(joukko1.ljono[i])
        for i in range(joukko2.alkioiden_lkm):
            uusi_joukko.lisaa(joukko2.ljono[i])

        return uusi_joukko

    @staticmethod
    def leikkaus(joukko1, joukko2):
        uusi_joukko = IntJoukko()

        for luku in joukko1.to_int_list():
            if joukko2.kuuluu(luku):
                uusi_joukko.lisaa(luku)
        
        return uusi_joukko

    @staticmethod
    def erotus(joukko1, joukko2):
        uusi_joukko = IntJoukko()

        for luku in joukko1.to_int_list():
            if not joukko2.kuuluu(luku):
                uusi_joukko.lisaa(luku)

        return uusi_joukko

    def __str__(self):
        return f"{{{', '.join([str(luku) for luku in self.ljono[:self.alkioiden_lkm]])}}}"
