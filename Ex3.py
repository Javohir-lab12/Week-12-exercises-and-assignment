# Format: Product, Stock, Minimum
data = """Apples,50,100
Bananas,120,100
Cherries,5,20
Dates,50,50
Eggs,10,24"""

# with open("inventory.csv", "w") as f:
#     f.write(data)
with open("inventory.csv", "r") as file:
    for line in file:
        product, stock, minimum = line.strip().split(",")
        stock = int(stock)
        minimum = int(minimum)
        if stock < minimum:
            with open("reorder_list.txt", "a") as orders:
                orders.write(f"Item: {product} | Order Amount: {minimum-stock}\n")