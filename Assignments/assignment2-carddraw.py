# Program that prints out 5 cards
# Author: Tihana Gray

import requests
# This is a Python library that allows us to make HTTP requests to APIs.
# 📚 References:
# https://realpython.com/python-requests/
# https://www.geeksforgeeks.org/python/python-requests-tutorial/
# https://www.w3schools.com/Python/module_requests.asp
# https://requests.readthedocs.io/en/latest/

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
# This is the URL for the API endpoint that shuffles a new deck of cards.
# 📚 Reference: https://deckofcardsapi.com/

response = requests.get(url)
# This line sends an HTTP GET request to the specified URL.
# The result is stored in the variable 'response'.
# 📚 References: 
# https://requests.readthedocs.io/en/latest/user/quickstart/
# https://www.geeksforgeeks.org/python/response-url-python-requests/

data = response.json()
# API returns JSON.
# .json() converts the JSON response into a Python dictionary.
# 📚 Reference: https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content

print(data)
# Checking the structure of the data returned by the API.
# Printed response: {'success': True, 'deck_id': '4t3z4u6f5c92', 'remaining': 52, 'shuffled': True}
# deck_id is a key that we will use to draw cards from the deck.

deck_id = data["deck_id"]
# Accessing the value associated with the key 'deck_id' from the data dictionary.
print(deck_id)

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
# Inserts deck_id value and requests 5 cards to be drawn from the deck.
# String formatting using f-strings allows us to easily construct the URL with the deck_id variable.
# 📚 References: 
# https://deckofcardsapi.com/#draw-a-card
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

response = requests.get(draw_url)
# Sends an HTTP GET request to the draw_url to draw 5 cards from the deck.
# Stores the response in the variable 'response'.
# 📚 References: 
# https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
# https://www.geeksforgeeks.org/python/response-json-python-requests/

draw_data = response.json()
# Converts the JSON response into a Python dictionary.
# JSON must be converted into native Python data structures before it can be accessed.
# 📚 Reference: https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content

print(draw_data)
# Outputs the entire draw response dictionary to the console and checks its structure.

cards = draw_data["cards"]
# Here we access the 'cards' in the 'draw_data' dictionary.
# It stores the associated list of card dictionairies in the variable 'cards'.
# 📚 Reference: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

for card in cards:
# 'for' loop iterates over each card in the 'cards' list.
# Each 'card' is a dictionary containing details about the card.
# 📚 Reference: https://docs.python.org/3/tutorial/controlflow.html#for-statements
    value = card["value"]
# Extracts the value field from the current card dictionary.
# Stores the value in the variable 'value'.
# 📚 Reference: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

suit = card["suit"]
# Accesses the value associated with the key 'suit' in the card dictionary.
# The value represents the card's suit and is a string.

print(value, "of", suit)
# Involves 3 separate arguments: the value of the card, the string "of", and the suit of the card.
# 📚 Reference: https://stackoverflow.com/questions/49682992/python-printing-from-a-list-that-contains-values-from-a-class

values = []
suits = []
# Creating empty lists to store the values and suits of the drawn cards.

for card in cards:
    values.append(card["value"])
    # Extracts the value field from the dictionary and appends it to the list.
    # 📚 Reference: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    suits.append(card["suit"])
    # Extracts the suit field from the dictionary and appends it to the list.

print(values)
print(suits)
   