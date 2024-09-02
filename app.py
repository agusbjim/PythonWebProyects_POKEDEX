import requests
from flask import Flask, render_template

app = Flask(__name__)

# URL to the PokeAPI for fetching Pokémon data
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"

# Function to fetch the list of Pokémon (default limit set to 151)
def fetch_all_pokemon(limit=151):
    response = requests.get(f"{POKEAPI_URL}?limit={limit}")
    if response.status_code == 200:
        data = response.json()
        return data['results']
    return []

# Function to fetch details of a specific Pokémon by ID
def fetch_pokemon_details(pokemon_id):
    response = requests.get(f"{POKEAPI_URL}/{pokemon_id}")
    if response.status_code == 200:
        return response.json()
    return None

# Route to display the main page with a list of Pokémon
@app.route('/')
def index():
    pokemon_list = fetch_all_pokemon()
    return render_template('index.html', pokemon_list=pokemon_list)

# Route to display details of a specific Pokémon
@app.route('/pokemon/<int:pokemon_id>')
def pokemon_detail(pokemon_id):
    pokemon = fetch_pokemon_details(pokemon_id)
    if pokemon:
        return render_template('pokemon.html', pokemon=pokemon)
    else:
        return "Pokémon not found", 404

if __name__ == '__main__':
    app.run(debug=True)
