import random

trollNum = random.randint(1,2)
counter = 1
print("Try to guess my secret number!")
answer =int( raw_input())
while answer != trollNum:
	if answer == trollNum:
		counter = counter + 1
		print("Good guess, you win!")
	if answer > trollNum:
		print("Too high! Guess again.")
		answer = int(raw_input())
		counter = counter + 1
	elif answer < trollNum:
		print("Too low! Guess again.")
		answer = int (raw_input())
		counter = counter + 1

if counter == 1:
	print("You got " + str(100) + " points! You win! ")
else:
	print("You got " + str(100 / counter) + " points! You win! ")

	







