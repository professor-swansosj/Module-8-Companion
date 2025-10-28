"""
TODO: Complete this dad joke fetching script
Hint: Use the requests library to fetch jokes from an API
"""

import requests
import json
import random

def fetch_dad_joke():
    """
    TODO: Fetch a dad joke from the API
    Hint: Use https://icanhazdadjoke.com/ API
    Set headers: {'Accept': 'application/json'}
    """
    # TODO: Make API request and return joke text
    pass

def fetch_programming_joke():
    """
    TODO: Fetch a programming joke as alternative
    Hint: Use https://official-joke-api.appspot.com/random_joke
    This returns JSON with setup and punchline
    """
    # TODO: Fetch programming joke and format it nicely
    pass

def display_joke_with_style(joke_text):
    """
    TODO: Display the joke with ASCII art borders
    Hint: Create a nice border around the joke text
    """
    # TODO: Make the joke display look awesome!
    # Add borders, emojis, or ASCII art
    pass

def handle_network_error():
    """
    TODO: Handle case when internet is not available
    Hint: Display a fallback joke or error message
    """
    fallback_jokes = [
        "Why don't containers ever get lost? Because they always know their image!",
        "What did the Docker container say to the VM? You're too heavy, I travel light!",
        "Why do network engineers love containers? Because they're always in a good network!"
    ]
    # TODO: Display a random fallback joke
    pass

def main():
    """Main joke fetching function"""
    print("🎭 Dad Joke Container Service")
    print("=" * 40)
    
    # TODO: Try to fetch jokes, handle errors gracefully
    # 1. Try to fetch a dad joke
    # 2. If that fails, try programming joke
    # 3. If all fails, show fallback joke
    # 4. Display with style!
    
    pass

if __name__ == "__main__":
    main()