import requests
import json


ico = input("Zadejte IČO subjektu: ")

response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")

data = response.json()

obchodni_jmeno = data.get('obchodniJmeno', 'Neznámé obchodní jméno')

adresa = data.get('sidlo', {}).get('textovaAdresa', 'Neznámá adresa')

print(f"Obchodní jméno: {obchodni_jmeno}")
print(f"Adresa: {adresa}")





nazev_subjektu = input("Zadejte název subjektu k vyhledání: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = f'{{"obchodniJmeno": "{nazev_subjektu}"}}'


response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

vysledek = response.json()

pocet_subjektu = vysledek.get("pocetCelkem", 0)
print(f"Nalezeno subjektů: {pocet_subjektu}")

if pocet_subjektu > 0:
    subjekty = vysledek.get("ekonomickeSubjekty", [])
    for subjekt in subjekty:
        obchodni_jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
        ico = subjekt.get("ico", "Neznámé IČO")
        print(f"{obchodni_jmeno}, {ico}")
else:
    print("Nebyl nalezen žádný subjekt s tímto názvem.")






