import requests
import concurrent.futures

# Base URLs
base_url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
type_url = "https://pokeapi.co/api/v2/type/"  # Base URL for types
types_list_url = "https://pokeapi.co/api/v2/type"  # URL to fetch available types

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

# Function to fetch the available Pokémon types from the API
def fetch_pokemon_types():
    try:
        response = requests.get(types_list_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error fetching Pokémon types: {err}")
        return []

    # Parse the JSON response
    data = response.json()

    # Return a list of types
    return [type_info['name'] for type_info in data['results']]

# Function to fetch the list of Pokémon based on the type
def get_pokemon_by_type(pokemon_type):
    try:
        if pokemon_type == "all":
            # Fetch all Pokémon
            response = requests.get(base_url)
        else:
            # Fetch Pokémon by type
            response = requests.get(f"{type_url}{pokemon_type}")
        
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return []

    # Parse the JSON response
    data = response.json()

    # If fetching all Pokémon, handle differently from types
    if pokemon_type == "all":
        pokemon_list = data['results']  # 'results' contains all Pokémon details
    else:
        pokemon_list = data['pokemon']  # 'pokemon' contains Pokémon for a specific type
    
    # Simplified list of Pokémon with names and URLs
    simplified_pokemon_list = [{"name": pokemon['pokemon']['name'], "url": pokemon['pokemon']['url']} for pokemon in pokemon_list] if pokemon_type != "all" else [{"name": pokemon['name'], "url": pokemon['url']} for pokemon in pokemon_list]
    
    print(f"Fetched {len(simplified_pokemon_list)} {pokemon_type.capitalize()}-type Pokémon.")
    return simplified_pokemon_list

# Function to fetch and print details of Pokémon concurrently
def fetch_filtered_pokemon_details(pokemon_list):
    # Use ThreadPoolExecutor to fetch details concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fetch_pokemon_details, pokemon_list)
    
    # Print all Pokémon details
    for result in results:
        print(result)

# Main execution logic
def main():
    # Fetch available Pokémon types dynamically
    pokemon_types = fetch_pokemon_types()

    # Add the option to fetch all Pokémon
    pokemon_types.append("all")

    # Display the types dynamically
    print("Choose a Pokémon type to fetch:")
    for i, p_type in enumerate(pokemon_types):
        print(f"{i+1}. {p_type.capitalize()} Pokémon")

    # Ask the user for their choice
    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > len(pokemon_types):
            raise ValueError
        pokemon_type = pokemon_types[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Fetching all Pokémon by default.")
        pokemon_type = "all"

    # Fetch the list of Pokémon based on the user's choice
    pokemon_list = get_pokemon_by_type(pokemon_type)

    # Fetch and print details of the selected Pokémon
    fetch_filtered_pokemon_details(pokemon_list)

# Run the main function
if __name__ == "__main__":
    main()
