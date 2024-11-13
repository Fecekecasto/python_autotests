import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aa1ab6bb9c405cecf91487195c4ca28c'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
create_pokemon = {"name": "Name", "photo_id": -1}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemon) #Создаётся покемон с именем Name
print(response.text)

data = response.json() #Преобразуем ответ в JSON
    
poke_id = data['id'] #Извлекаем переменную id

print(f'ID покемона: "{poke_id}"') #Переменная успешно извлечена

pokemon_name = {"pokemon_id": poke_id, "name": "Python", "photo_id": -1} #Вводим переменную для запроса на переименование и поимку именно здесь, иначе id не читается

response2 = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = pokemon_name) #Переименуем созданного ранее покемона в Python
print(response2.text)

catch = {"pokemon_id": poke_id}

response3 = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = catch) #Поймаем созданного ранее покемона
print(response3.text)