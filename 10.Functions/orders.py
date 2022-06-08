def orders(product: str, quantity: int):
    price = 0
    if product == "coffee":
        price = 1.5 * quantity
    elif product == "coke":
        price = 1.4 * quantity
    elif product == "water":
        price = 1 * quantity
    elif product == "snacks":
        price = 2 * quantity
    return price


type_of_product = input()
product_quantity = int(input())

print(f"{orders(product=type_of_product, quantity=product_quantity):.2f}")
