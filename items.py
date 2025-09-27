item = input("What item would you like? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like?"))

total = price * quantity

print(f"You have bought {quantity} of the {item}'s.")
print(f"Your total is: ${round(total, 2)}")