# Program that prints out 5 cards and talks like a pirate.
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

value_counts = {}
# This creates an emty dictionary called value_counts.
# It is needed to know how many times each count appears.
# 📚 References: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://stackoverflow.com/questions/17709270/create-column-of-value-counts-in-pandas-dataframe

for value in values:
# This loop iterates over each value in the values list.
    if value in value_counts: # This line checks if the current card value exists.
        value_counts[value] += 1 # Increases the count by 1.
    else:
        value_counts[value] = 1 # Creates new dictionary entry with a count of 1.
# 📚 References: https://docs.python.org/3/reference/expressions.html#membership-test-operations
# https://docs.python.org/3/tutorial/controlflow.html#for-statements
# https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

counts = value_counts.values()
# This line retrieves the counts of each card value from the value_counts dictionary.
# 📚 Reference: https://docs.python.org/3/library/stdtypes.html#dict.values

if 3 in counts: # This line checks if there are 3 cards of the same value in the hand.
    print("Ahoy, pirate! Three o' the same, the sea favors ye today!")
elif 2 in counts: # This line checks if there are 2 cards of the same value in the hand.
    print("Shiver me timbers! A pair be in yer grasp! A grand haul, indeed.")
# 📚 References: https://docs.python.org/3/tutorial/controlflow.html#if-statements
# https://docs.python.org/3/reference/expressions.html#membership-test-operations
# https://www.w3schools.com/python/gloss_python_elif.asp

if len(set(suits)) == 1: # This line checks if all the suits in the hand are the same.
    print("By the beard of Blackbeard, ye’ve struck gold! All cards be of the same suit! A flush, ye say?")
# 📚 References: https://docs.python.org/3/tutorial/datastructures.html#sets
# https://docs.python.org/3/library/functions.html#len
# https://realpython.com/len-python-function/

value_map = {
    "ACE": 14,
    "KING": 13,
    "QUEEN": 12,
    "JACK": 11
}
# This part creates a dictionary that maps the face card values to their corresponding numerical values.
# Straight detection requires numerical values to compare the cards.
# 📚 Reference: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

numeric_values = []
# This creates an empty list to store the numeric values of the cards.  
# 📚 Reference: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

for value in values:
    if value in value_map:
        numeric_values.append(value_map[value]) # If the value is a face card, append its mapped numeric value.
    else:
        numeric_values.append(int(value)) # If it's a number card, convert it to an integer and append it.
# 📚 References: https://www.geeksforgeeks.org/python/python-if-else/
# https://www.geeksforgeeks.org/python/python-list-append-method/
# https://realpython.com/python-append/
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# https://docs.python.org/3/library/functions.html#int

numeric_values.sort() # Sorts the list in ascending order to check for straights.
# 📚 Reference: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

is_straight = True # This is the initial assumption that the hand is a straight until proven otherwise.
for i in range(1, len(numeric_values)): # This loop iterates through the sorted numeric values starting from the second card.
    if numeric_values[i] != numeric_values[i-1] + 1: # This condition checks if the current card value is not exactly 1 greater than the previous card value.
        is_straight = False # If the condition is true, it means the cards are not in a sequence, so we set is_straight to False.
        break # Exits the loop early since we have already determined that the hand is not a straight.
# 📚 References: https://docs.python.org/3/library/functions.html#func-range
# https://docs.python.org/3/library/functions.html#len
# https://docs.python.org/3/reference/expressions.html#comparisons
# https://docs.python.org/3/reference/simple_stmts.html#the-break-statement

if is_straight: # If the is_straight variable is still True after the loop, it means all cards are in a sequence.
    print ("Luck be sailin’ with ye! A straight be in yer hand, the winds be in yer favor!")
    
if not (3 in counts or 
        2 in counts or 
        len(set(suits)) == 1 or 
        is_straight):
    print("Deal again and test yer fate!")
# This condition checks if none of the winning conditions are met (no three of a kind, no pair, no flush, no straight).
# If none of these conditions are true, it prints a message encouraging the player to try again.
# 📚 References: https://docs.python.org/3/tutorial/controlflow.html#if-statements  
# https://docs.python.org/3/reference/expressions.html#membership-test-operations
# https://docs.python.org/3/library/functions.html#len  