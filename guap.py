# for every roll of paper towels, you get a $0.25 rebate
# but if you buy more than ten rolls, you get a $0.35 rebate for each one
print("How many rolls of paper towels did you buy")
rolls = int(raw_input())
 
print("Are you a value club member? Respond yes or no.")
club = raw_input()
if club == "yes":
        print("In the club")
	if rolls > 10:
		rebate = rolls * .35 + 2
	else:
		rebate = rolls * .25 + 2	

else:
        print("not in the club")
	if rolls > 10:
		rebate = rolls * .35
	else:
		rebate = rolls * .25
#print rebate
print("Your rebate is $" + str(rebate))
   

