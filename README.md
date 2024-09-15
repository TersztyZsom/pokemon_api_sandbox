# Pokémon API Water-Type Fetcher

This Python program fetches and prints detailed information about all water-type Pokémon from the Pokémon API ([PokeAPI](https://pokeapi.co/)). It retrieves the Pokémon’s ID, name, height, weight, and base experience using a concurrent fetching method to ensure quick and efficient data retrieval.

## Features

- Fetches a list of all **water-type Pokémon** from the PokeAPI.
- Concurrently fetches details for each water-type Pokémon (using Python’s `concurrent.futures`).
- Outputs key details for each Pokémon:
  - ID
  - Name
  - Height
  - Weight
  - Base experience

## How It Works

1. **Fetch Water-Type Pokémon List**: 
   The program starts by retrieving a list of all water-type Pokémon from the PokeAPI using the `/type/water` endpoint. This list provides basic information, including each Pokémon’s name and a URL to fetch more details.

2. **Fetch Pokémon Details Concurrently**: 
   After fetching the list, the program concurrently fetches detailed information for each water-type Pokémon. The concurrent approach ensures that the program retrieves all details as quickly as possible without overloading the API with requests.

3. **Print Pokémon Details**:
   For each Pokémon, the program prints the following:
   - ID
   - Name
   - Height
   - Weight
   - Base experience

### Example Output

```bash
Fetched 123 Water-type Pokémon.
ID: 7, Name: squirtle, Height: 5, Weight: 90, Base Experience: 63
ID: 8, Name: wartortle, Height: 10, Weight: 225, Base Experience: 142
ID: 9, Name: blastoise, Height: 16, Weight: 855, Base Experience: 239
...
