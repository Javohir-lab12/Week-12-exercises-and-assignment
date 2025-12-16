data = """Lunch,12.50
Coffee,5.00
Office Supplies,23.75
Taxi,10.00
Coffee,8.25
Dinner,50.00"""

# with open("expenses.txt", "w") as f:
#     f.write(data)
file = open("expenses.txt" , "r")
total = 0
counter = 0
for line in file:
    parts = line.strip().split(",")
    name = parts[0]
    cost = float(parts[1])
    total += cost
    counter += 1
file.close()
print("--- Expense Report ---")
print(f"Total Transactions: {counter}")
print(f"Total Spent: ${total}")
print(f"Average Expense: ${total / counter}")