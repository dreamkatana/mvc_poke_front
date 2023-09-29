from flask import render_template, request
import requests
import random
from . import app

# API COM A LISTA DE POKEMONS
BASE_URL = "https://pokeapi.co/api/v2/pokemon"

# Busca os 10 primeiros Pokemons e seus detalhes
def fetch_pokemon_list():
    # Randomly select 10 Pokémon
    offset = random.randint(1, 1000)
    response = requests.get(f"{BASE_URL}?limit=10&offset={offset}")
    pokemon_summaries = response.json()["results"]
    detailed_pokemons = [requests.get(poke["url"]).json() for poke in pokemon_summaries]
    return detailed_pokemons

# Busca o Pokemon pelo nome
def fetch_pokemon_detail(pokemon_name):
    response = requests.get(f"{BASE_URL}/{pokemon_name}")
    # Check if the request was successful
    if response.status_code != 200:
        response = requests.get(f"{BASE_URL}/pikachu")        
    
    try:
        return response.json()
    except ValueError:  # Handle non-JSON responses
        raise ValueError(f"Failed to decode API response as JSON: {response.text}")
    
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pokemon_name = request.form.get('search').lower()
        # Popula o banco de dados com o pokemon pesquisado
        ip_address = request.remote_addr  # Get client IP address

        # Create the request body
        body = {
            "ip_address": ip_address,
            "pokemon_name": pokemon_name
        }
        response = requests.post('http://searches_service:5001/searches', json=body)
        searched_pokemon = [fetch_pokemon_detail(pokemon_name)]
        return render_template('principal.html', pokemons=searched_pokemon)
    return render_template('principal.html', pokemons=fetch_pokemon_list())

@app.route("/home")
def inicio():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/estatisticas/")
def estatistica():
    response = requests.get("http://searches_service:5001/searches")
    searches = response.json()
    return render_template('estatistica.html', searches=searches)
