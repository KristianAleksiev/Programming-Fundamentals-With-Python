inventory = input().split()
products = {inventory[i]: int(inventory[i+1]) for i in range(0, len(inventory), 2)}

products_to_search = input().split()

for product in products_to_search:
    if product not in products:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {products[product]} of {product} left")
