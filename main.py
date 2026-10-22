from product_functions import collect_products, show_product
from storage import load_products, save_product

# load previously stored products
all_products = load_products()

#collect new products
new_products = collect_products()

#add new products to the existing list of products
all_products.extend(new_products)

#save the complete added 
save_product(all_products)

#display the product summary
for product in all_products:
    show_product(product)
