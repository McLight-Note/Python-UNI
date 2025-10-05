import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = 'typhlosion'
pokemon_ifno = get_pokemon_info(pokemon_name)

if pokemon_ifno:
    print(f"Name: {pokemon_ifno['name'].capitalize()}")
    print(f"ID: {pokemon_ifno['id']}")
    print(f"Height: {pokemon_ifno['height']}")
    print(f"Weight: {pokemon_ifno['weight']}")