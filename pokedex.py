import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name: str):
    
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"Failed to retrieve data {response.status_code}")