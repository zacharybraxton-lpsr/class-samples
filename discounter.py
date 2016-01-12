# find out price from user
print("What's the price")
price = int(raw_input())

# calculate discount price
discount_price = price - (.10 * price)

# if user gets a discount, tell them
# if not, tell them
if price > 10:
	print("You're price is " + str(discount_price) + " ")
