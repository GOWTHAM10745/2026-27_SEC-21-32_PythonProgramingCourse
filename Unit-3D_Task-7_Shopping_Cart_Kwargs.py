def shopping_cart(**products): 
    total = int(input("total:"))
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total = int(input("total:"))
    print(f"Total: ₹{total}")
shopping_cart(apple=15, orange=12, mango=10)  