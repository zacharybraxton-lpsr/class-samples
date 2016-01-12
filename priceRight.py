print("How much money did you spen at Python's Super Tech Store?")
spent = int(input())
print("You spent this much money in cents:")
print(spent * 100)

price2 = spent * 100
discount = price2 * .1
fullDiscount = price2 - discount
discount2 = int(fullDiscount)

if price2 > 1000:
    print("Because you spent over $10 you get a discount! You only have to pay: " + str(discount2) + " !")

if price2 <= 1000:
    print("Because you spent $10 or less you didn't get a discount... sorry")

