foods = []
prices = []
total = 0

while True:
    food = input("Enter food items to buy (enter q to quit) : ")
    if food.strip().lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("\n-------- YOUR CART --------")
print(f"{'Item'.ljust(20)}{'Price'}")
print("-" * 30)

for food, price in zip(foods, prices):
    print(f"{food.ljust(20)}${price:>7.2f}")

total = sum(prices)

print("-" * 30)
print(f"{'Total'.ljust(20)}${total:>7.2f}")


""" 
foods = []
prices = []
total = 0

while True:
    food = input("Enter food items to buy (enter q to quit) :: ")
    if food.strip().lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("-------- YOUR CART --------")
# Set a width for alignment
item_width = max(len(food) for food in foods) + 2  # Adjust width as needed
price_width = 10  # Fixed width for prices

for food, price in zip(foods, prices):
    print(f"{food:<{item_width}}{price:>{price_width}.2f}")

total = sum(prices)
print("-" * (item_width + price_width))
print(f"{'Total:':<{item_width}}${total:>{price_width - 1}.2f}")


"""