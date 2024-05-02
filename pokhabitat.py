import requests

# definir le endpoint de l'API
url = "https://pokeapi.co/api/v2/pokemon-habitat"

# definir une variable qui contiens le resultat de l'API
liste = requests.get(url)

# verifier le statut de la reponse : 200 veut dire bonne reponse
if liste.status_code == 200:
    inf = liste.json()

#{'name': 'mountain', 'url': 'https://pokeapi.co/api/v2/pokemon-habitat/4/'}
    l = inf['results']
    for e in l:
        print(e["name"])
    # apokliste = [pokemon['name'] for pokemon in inf['pokemon-habitat']]


else:
    # Si le code n'est pas 200 affiche un message d'erreur
    print("Erreur API")