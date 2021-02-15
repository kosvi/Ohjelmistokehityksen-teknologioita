#!/usr/bin/python3

# Ladataan tarvittavat moduulit
import logiikka

# Tämä on varsinainen main-metodi, josta koko sovellus alkaa
def menu():
    print("Tervetuloa!")
    postinumerodata = None
    # printataan menu ja luupataan sitä kunnes käyttäjä haluaa poistua
    while True:
        tulosta_menu()
        komento = input("> ").lower()
        if komento=="exit":
            break
        if komento=="lataa":
            postinumerodata = logiikka.hae_postinumerodata()
        if komento=="etsi":
            # Etsi komento tarkistaa postinumerodatan, eikä etene jos sitä ei vielä ole ladattu
            etsi(postinumerodata)
    print("\nHeippa!")

def etsi(postinumerodata):
    # Ei tehdä mitään, jos postinumeroissa ei ole dataa
    if postinumerodata==None:
        print("\n\tPostinumerodataa ei ole ladattu...")
        return
    print("")
    # Muussa tapauksessa luupataan, ellei käyttäjä halua takaisin
    print("Lopeta hakeminen komennolla: takaisin")
    while True:
        print("Anna hakusana: (postinumero tai toimipaikka)")
        hakusana = input("> ").lower()
        if hakusana=="takaisin" or hakusana=="exit":
            break
        # Jos syötteen voi muuttaa integeriksi, se on postinumero
        # Tehdään kiero tarkastus ja päätellään siitä, mitä käyttäjä on hakemassa
        try:
            int(hakusana)
            hakutulos = logiikka.etsi_postitoimipaikka(postinumerodata, hakusana)
            if hakutulos!= None:
                print(f'Postinumerolla {hakusana} löytyi postitoimipaikka {hakutulos.capitalize()}\n')
            else:
                print("Antamallasi numerolla ei löytynyt postitoimipaikkaa.\n")
        except: 
            hakutulos = logiikka.etsi_postinumerot(postinumerodata, hakusana)
            if hakutulos:
                # saatiin lista, joka ei ole tyhjä
                print(f'Postitoimipaikalle {hakusana.capitalize()} löydettiin seuraavat postinumerot: ')
                numerot = ", ".join(hakutulos)
                print(numerot)
                print("")
            else:
                print("Antamallasi hakusanalla ei löytynyt postinumeroita.\n")

# Tässä printataan main-menu käyttäjälle
def tulosta_menu():
    print("")
    print("Komennot: ")
    print("lataa \t\t- lataa postinumerodata verkosta")
    print("etsi \t\t- etsi postinumero tai postitoimipaikka")
    print("exit \t\t- poistu sovelluksesta")

if __name__ == "__main__":
    menu()

