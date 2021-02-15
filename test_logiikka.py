#
# En muista miten mocker-dataa luennolla käytettiin, mutta en keksinyt miten sitä käyttää
# oman sovellukseni testaamisessa, koska datan hakeminen on eriytetty omaksi metodiksi
# ja pystyn hyvin syöttämään mock-datan suoraan parametsina etsimis-funktioille
# 

import logiikka

MOCKDATA = {
    "33340": "TAMPERE",
    "33101": "TAMPERE",
    "00930": "HELSINKI",
    "44884": "SMART POST",
    "33720": "TAMPERE",
}

def test_etsi_postitoimipaikka_33340():
    toimipaikka = logiikka.etsi_postitoimipaikka(MOCKDATA, "33340")
    assert toimipaikka == "TAMPERE"

def test_etsi_postitoimipaikka_44884():
    toimipaikka = logiikka.etsi_postitoimipaikka(MOCKDATA, "44884")
    assert toimipaikka == "SMART POST"

def test_etsi_postitoimipaikka_00000():
    toimipaikka = logiikka.etsi_postitoimipaikka(MOCKDATA, "00000")
    assert toimipaikka == None

# Testataan myös, että höpöhöpösyote ei kaada ohjelmaa
def test_etsi_postitoimipaikka_foo():
    toimipaikka = logiikka.etsi_postitoimipaikka(MOCKDATA, "foo")
    assert toimipaikka == None

def test_etsi_postinumerot_tampere():
    hakusana = "tampere"
    numerot = logiikka.etsi_postinumerot(MOCKDATA, hakusana)
    assert numerot == ["33340", "33101", "33720"]
    numerot = logiikka.etsi_postinumerot(MOCKDATA, hakusana.upper())
    assert numerot == ["33340", "33101", "33720"]
    numerot = logiikka.etsi_postinumerot(MOCKDATA, hakusana.capitalize())
    assert numerot == ["33340", "33101", "33720"]

def test_etsi_postinumerot_smart_post():
    numerot = logiikka.etsi_postinumerot(MOCKDATA, "Smart Post")
    assert numerot == ["44884"]

def test_etsi_postinumerot_foo():
    numerot = logiikka.etsi_postinumerot(MOCKDATA, "foo")
    assert numerot == []

# Katsotaan vielä, että tyhjällä datalla palautuu None molemmista funktioista

def test_etsi_postitoimipaikka_none():
    toimipaikka = logiikka.etsi_postitoimipaikka(None, "33340")
    assert toimipaikka == None

def test_etsi_postinumerot_none():
    numerot = logiikka.etsi_postitoimipaikka(None, "Helsinki")
    assert numerot == None

