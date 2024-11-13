import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aa1ab6bb9c405cecf91487195c4ca28c'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
create_pokemon = {"name": "generate", "photo_id": -1}
pokemon_rename = {"pokemon_id": "131290", "name": "generate", "photo_id": -1}
catch_pokemon = {"pokemon_id": "131290"}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemon) 
print(response.text)

response2 = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = pokemon_rename) 
print(response2.text)

response3 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch_pokemon) 
print(response3.text)