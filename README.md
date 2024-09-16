
### README for Pokémon API Fetcher

## Pokémon API Fetcher

This Python script allows users to fetch details about Pokémon using the [PokéAPI](https://pokeapi.co/). Users can select to retrieve details for either all available Pokémon or filter them by type, such as Water or Fire types. The script performs concurrent fetching to improve performance when handling a large number of Pokémon.

## Features

- **Fetch All Pokémon**: Retrieve the complete list of all Pokémon available in the API.
- **Fetch Pokémon by Type**: Dynamically fetch a list of Pokémon based on type (Water, Fire, etc.).
- **Concurrency**: Fetches Pokémon details concurrently for faster performance.
- **Error Handling**: Handles errors like network issues or invalid user input gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TersztyZsom/pokemonapisandbox.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pokemonapisandbox
   ```
3. Install the required Python packages
 

## Usage

Run the script by using the following command:
```bash
python pokemonapisandbox.py
```

When you run the script, it will display a list of Pokémon types dynamically fetched from the API. You can choose a Pokémon type or select "All Pokémon" to fetch the entire list. The details of each Pokémon, including their ID, name, height, weight, and base experience, will be displayed.

### Example:
```
Choose a Pokémon type to fetch:
1. Normal Pokémon
2. Water Pokémon
3. Fire Pokémon
...
Enter your choice: 2

Fetched 151 Water-type Pokémon.
ID: 7, Name: squirtle, Height: 5, Weight: 90, Base Experience: 63
...
```

## Code Structure

- **`pokemonapisandbox.py`**: The main script that interacts with the PokéAPI to fetch Pokémon details based on user input.

## Dependencies

- **Python 3.x**
- **`requests`**: A simple HTTP library to make API requests.
- **`concurrent.futures`**: Used for concurrent fetching of data.

Install the dependencies by running

## Configuration

There are no major configurations needed for this script. If needed, you can modify the base API URLs in the script (though they are unlikely to change).

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
Here is a picture when you ran the program:



![image](https://github.com/user-attachments/assets/f0f99e75-ec1b-4aec-901c-1f5be0fb6018)


