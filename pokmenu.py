import requests

# Définir l'URL de l'API
url = "https://pokeapi.co/api/v2/pokemon-habitat/waters-edge/"

# Faire une requête GET à l'API
reponse = requests.get(url)

# Vérifier si la réponse est réussie (statut 200)
if reponse.status_code == 200:
    # Extraire les données JSON de la réponse
    donnees = reponse.json()

    # Extraire les noms des Pokémon de la clé "pokemon_species" et les stocker dans une liste
    liste = [pokemon['name'] for pokemon in donnees['pokemon_species']]
    
    # Afficher la liste des noms des Pokémon
    for nom in liste:
            print(nom)
    

else:
    # Si la réponse n'est pas réussie, afficher un message d'erreur
    print("Erreur lors de la requête à l'API:", reponse.status_code)