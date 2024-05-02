import requests
import json

# definir le endpoint de l'API
url = "https://pokeapi.co/api/v2/pokemon-habitat/waters-edge/"


# definir une variable qui contiens le resultat de l'API
liste = requests.get(url)

# verifier le statut de la reponse : 200 veut dire bonne reponse
if liste.status_code == 200:
    inf = liste.json()
    print(inf)

