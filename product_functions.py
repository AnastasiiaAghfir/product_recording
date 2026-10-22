def get_product():
    product_name = input('Enter product name please ')

    ##########################################################################
    # try ...  except  (аналог try ... catch в javascript)
    while True:
        try: 
            product_price = float(input('Enter a product price please '))
            if product_price < 0:
                print('Price cannot be negative.')
            else:
                break
        except ValueError:
            print('Invalid price. Please enter number.')
    ##########################################################################

    ##########################################################################
    # try ...  except  (аналог try ... catch в javascript)
    while True:
        try: 
            product_stock = int(input('Enter a stock quantity please '))
            if product_stock < 0:
                print('Quantity cannot be negative.')
            else:
                break
        except ValueError:
            print('Invalid quantity. Please enter whole number.')
    ##########################################################################

    
    return {
        'name': product_name,
        'price': product_price,
        'stock': product_stock,
    }
        
def collect_products():
    list_of_products = []
    add_new = 'yes'
    while True:
        if add_new.lower().strip() == 'yes': # убираем пробелі и приводим к одному регистру
            new_product = get_product()
            list_of_products.append(new_product)
        elif add_new.lower().strip() == 'no': # убираем пробелі и приводим к одному регистру
            break
        else:
            print('Unsupported response!!')
        add_new = input('Add another product? yes/no ')
    return list_of_products
    
def show_product(product):
    
    for key, value in product.items():
        if key == 'price':
            print(f'{key.capitalize()}: € {value:.2f}') # робить обмеження кількості символів після коми
        elif key == 'stock':
            print(f'{key.capitalize()}: {value} units')
        else:
            print(f'{key.capitalize()}: {value.capitalize()}')

