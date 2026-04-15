grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
"Eggs": ("Dairy", 5.50, 30),
"Bread": ("Bakery", 2.99, 15),
"Apples": ("Produce", 1.50, 50)}
price_of_eggs = grocery_inventory["Eggs"][1]
print(price_of_eggs)
if price_of_eggs >= 5.5:
     print("Eggs are too expensive, reducing the price by $1.")
     category, _, stock = grocery_inventory["Eggs"]
     grocery_inventory["Eggs"] = (category, price_of_eggs - 1, stock)
else:
    print("The price of Eggs is reasonable.")
print(grocery_inventory["Eggs"][1])
# replace line 11 with
grocery_inventory.update({ "Tomatoes": ("Produce", 1.20, 30) })
print("Inventory after adding Tomatoes:",grocery_inventory)


