import requests
import json
import pandas as pd

# API URLs
products_url = "https://fakestoreapi.com/products"
users_url = "https://fakestoreapi.com/users"
carts_url = "https://fakestoreapi.com/carts"

# Fetch data
products = requests.get(products_url).json()
users = requests.get(users_url).json()
carts = requests.get(carts_url).json()

# Save as JSON files
with open("products.json", "w") as f:
    json.dump(products, f)

with open("users.json", "w") as f:
    json.dump(users, f)

with open("carts.json", "w") as f:
    json.dump(carts, f)

print("Data saved successfully!")
