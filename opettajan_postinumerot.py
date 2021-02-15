import http_pyynto


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        korjattu_nimi = nimi
        korjattu_nimi = korjattu_nimi.replace(" ", "");
        # Tämä viivan ottaminen lienee tosin turhaa, mutta tehty mikä tehty
        korjattu_nimi = korjattu_nimi.replace("-", "")
        if korjattu_nimi not in paikat:
            paikat[korjattu_nimi] = []

        paikat[korjattu_nimi].append(numero)

    return yhdista_samankaltaiset(paikat)

# Typojen hanskaaminen on hankalaa, koska ihminen tietää heti, 
# että Helsikni on typo, mutta tietokone ei tiedä sitä.
# Tehdään oletus, että jos toimipaikka on muuten sama, mutta
# yksi peräkkäisten kirjaimien yhdistelmä on väärin päin, 
# on kyseessä typo. Etsitään siis toimipaikat, joiden nimet ovat 
# kahta merkkiä lukuunottamatta samat ja nämä kaksi poikkeavaa 
# merkkiä ovat peräkkäiset ja samat ristiin 

# Jälleen ongelmaksi jää, kumpi toimipaikka tulisi säilyttää: Helsinki vai Helsikni
# Vastaus: oletetaan, että useimmassa on kirjoitettu oikein ja säilytetään se, kummassa on 
# enemmän postinumeroita. 

def yhdista_samankaltaiset(toimipaikat):
    edellinen = ""
    for toimipaikka in sorted(toimipaikat):
        if len(edellinen)==len(toimipaikka):
            typo = tarkista_samankaltaisuus(edellinen, toimipaikka)
            if typo:
                edellinen_pituus = len(toimipaikat[edellinen])
                toimipaikka_pituus = len(toimipaikat[toimipaikka])
                if edellinen_pituus > toimipaikka_pituus:
                    toimipaikat[edellinen].extend(toimipaikat[toimipaikka])
                    del toimipaikat[toimipaikka]
                else:
                    toimipaikat[toimipaikka].extend(toimipaikat[edellinen])
                    del toimipaikat[edellinen]
        edellinen=toimipaikka
    return toimipaikat

def tarkista_samankaltaisuus(sana1, sana2):
    typo = False
    vaihdot = 0
    samat = 0
    if sana1[0]==sana2[0]:
        samat += 1
    for i in range(1, len(sana1)):
        if sana1[i]==sana2[i]:
            samat += 1
        if sana1[i]!=sana2[i]:
            if sana1[i]==sana2[i-1] and sana1[i-1]==sana2[i]:
                vaihdot += 1
    if samat == len(sana1)-2 and vaihdot == 1:
        typo = True
    return typo

def main():
    postinumerot = http_pyynto.hae_postinumerot()

    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

    toimipaikka = input('Kirjoita postitoimipaikka: ').strip().upper()
    # Koska siistimme avaimet dictionarysta, siistimme ne myös hakiessa sieltä
    toimipaikka = toimipaikka.replace(" ", "").replace("-", "")

    if toimipaikka in toimipaikat:
        toimipaikat[toimipaikka].sort()
    
        loydetyt_str = ', '.join(toimipaikat[toimipaikka])
        print('Postinumerot: ' + loydetyt_str)
    else:
        print('Toimipaikkaa ei löytynyt')

if __name__ == "__main__":
    main()

