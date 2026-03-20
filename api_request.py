import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
       
    else:
        print(f"Failed to retrive data {response.status_code}")


pokemon_name = input("Enter pokemon name: ")
pokemon_info =get_pokemon_info(pokemon_name)
# print(pokemon_info)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Height: {pokemon_info['height']}cm")
    print(f"Weight: {pokemon_info['weight']}kg")
    print(f"Id: {pokemon_info['id']}")
    