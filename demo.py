#!/usr/bin/env python3

from pprint import pprint
import requests

URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Generate an HTTP response
resp = requests.get(URL)

# Check if the response was successful
if resp.status_code == 200:
    # Parse JSON data
    data = resp.json()
    # Pretty print the data
    pprint(data)
else:
    # Print error details
    print(f"Failed to fetch data. Status code: {resp.status_code}")
    print(f"Response text: {resp.text}")
