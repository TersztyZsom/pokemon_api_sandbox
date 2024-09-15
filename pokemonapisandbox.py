import requests
import concurrent.futures

# Base URL to get the list of all Pokémon
base_url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
type_url = "https://pokeapi.co/api/v2/type/water"  # URL to get water-type Pokémon

# Function to fetch the details of a single Pokémon given its URL
def fetch_pokemon_details(pokemon):
    try:
        pokemon_data = requests.get(pokemon['url']).json()

        # Extract the needed details
        pokemon_info = {
            "id": pokemon_data['id'],
            "name": pokemon_data['name'],
            "weight": pokemon_data['weight'],
            "height": pokemon_data['height'],
            "base_experience": pokemon_data['base_experience']
        }

        # Return the details in a formatted string
        return f"ID: {pokemon_info['id']}, Name: {pokemon_info['name']}, Height: {pokemon_info['height']}, Weight: {pokemon_info['weight']}, Base Experience: {pokemon_info['base_experience']}"
    
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch details for {pokemon['name']}: {e}"

# Function to fetch the list of all "water" Pokémon
def get_water_pokemon():
    try:
        # Make the request to get the list of all "water" Pokémon
        response = requests.get(type_url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return []

    # Parse the JSON response
    data = response.json()
    water_pokemon_list = data['pokemon']
    
    # Get the simplified list with names and URLs
    simplified_pokemon_list = [{"name": pokemon['pokemon']['name'], "url": pokemon['pokemon']['url']} for pokemon in water_pokemon_list]
    print(f"Fetched {len(simplified_pokemon_list)} Water-type Pokémon.")

    return simplified_pokemon_list

# Function to fetch and print details of filtered Pokémon concurrently
def fetch_filtered_pokemon_details(pokemon_list):
    # Use ThreadPoolExecutor to fetch details concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fetch_pokemon_details, pokemon_list)
    
    # Print all Pokémon details
    for result in results:
        print(result)

# Fetch and print only Water-type Pokémon details
water_pokemon_list = get_water_pokemon()
fetch_filtered_pokemon_details(water_pokemon_list)
