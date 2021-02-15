# Ladataan tarvittavat moduulit
import json
import urllib.request

def etsi_postitoimipaikka(postinumerodata, postinumero):
    # Ei tehdä mitään, jos postinumeroissa ei ole dataa
    if postinumerodata==None:
        return None
    paikka = postinumerodata.get(postinumero, None)
    return paikka

def etsi_postinumerot(postinumerodata, hakusana):
    # Ei tehdä mitään, jos postinumeroissa ei ole dataa
    if postinumerodata==None:
        return None
    numerot = []
    # data on all caps, eli hakusana myös
    hakusana = hakusana.upper()
    for numero, paikka in postinumerodata.items():
        if paikka==hakusana:
            numerot.append(numero)
    return numerot

def hae_postinumerodata():
    # Tämä urlin lataaminen on kyllä ihan 1:1 Pythonin dokumentaatioista
    try:
        with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
            json_data = response.read()
        json_data = json.loads(json_data)
        return json_data
    except:
        return None

