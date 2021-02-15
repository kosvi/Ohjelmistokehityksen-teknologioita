import opettajan_postinumerot

MOCKDATA = {
    "33340": "TAMPERE",
    "33101": "TAMPERE",
    "00930": "HELSINKI",
    "44884": "SMART POST",
    "33720": "TAMPERE",
    "00314": "SMARTPSOT",
    "70304": "SMARTPOST",
    "54550": "SUO-ANTTILA",
}

# SMARTPSOT ON LYHYEMPI JA SE LIITETÄÄN SMARTPOSTin PERÄÄN SEKÄ POISTETAAN
# SUO-ANTTILASTA lähtee väliviiva pois

RYHMITELTY_MOCKDATA = {
    "TAMPERE": ["33340", "33101", "33720"], 
    "HELSINKI": ["00930"], 
    "SMARTPOST": ["44884", "70304", "00314"],
    "SUOANTTILA": ["54550"]}

def test_ryhmittele_toimipaikoittain():
    toimipaikat = opettajan_postinumerot.ryhmittele_toimipaikoittain(MOCKDATA)
    assert toimipaikat == RYHMITELTY_MOCKDATA

