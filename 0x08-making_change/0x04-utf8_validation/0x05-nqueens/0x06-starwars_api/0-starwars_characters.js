#!/usr/bin/node
import requests
import sys

def get_movie_characters(movie_id):
    base_url = "https://swapi.dev/api"
    
    # Make a request to get information about the specified movie
    movie_url = f"{base_url}/films/{movie_id}/"
    response = requests.get(movie_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        movie_data = response.json()

        # Get the list of characters in the movie
        characters_urls = movie_data['characters']

        # Iterate through characters and print their names
        for character_url in characters_urls:
            character_data = requests.get(character_url).json()
            print(character_data['name'])
    else:
        print(f"Failed to retrieve movie data. Status Code: {response.status_code}")

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <Movie_ID>")
        sys.exit(1)

    try:
        movie_id = int(sys.argv[1])
    except ValueError:
        print("Movie_ID must be a number")
        sys.exit(1)

    # Call the function to get and print characters
    get_movie_characters(movie_id)

if __name__ == "__main__":
    main()