from kps import KpsTekoaly, KpsParempiTekoaly, KpsPelaajaVsPelaaja


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()[-1]
        PELIT = {"a": KpsPelaajaVsPelaaja(), "b": KpsTekoaly(), "c": KpsParempiTekoaly()}

        if not vastaus in PELIT:
            break

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        peli = PELIT[vastaus]
        peli.pelaa()

if __name__ == "__main__":
    main()
