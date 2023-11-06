import requests
import sys

def get_movie_characters(movie_id):
    # Fetch movie details from the Star Wars API
    movie_url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(movie_url)

    if response.status_code == 200:
        movie_data = response.json()
        characters = movie_data['characters']
        print(f"Characters in {movie_data['title']} (Episode {movie_data['episode_id']}):")
        
        # Fetch and display character names
        for character_url in characters:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_data = character_response.json()
                print(character_data['name'])
            else:
                print(f"Failed to fetch character data for {character_url}")
    else:
        print("Failed to fetch movie data")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the Movie ID as an argument (e.g., 3 for 'Return of the Jedi')")
    else:
        movie_id = sys.argv[1]
        get_movie_characters(movie_id)
