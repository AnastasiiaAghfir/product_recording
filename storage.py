import json

def load_products():
    with open('products.json', 'r', encoding = 'utf-8') as file:
        products = json.load(file)
    return products

def save_product(products):
    with open('products.json', 'w', encoding = 'utf-8') as file:
        json.dump(products, file, indent = 4, ensure_ascii = False)