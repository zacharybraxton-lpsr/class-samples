print("How old are you?")
age = int(raw_input())

print("What is your GPA")
GPA = float(raw_input())
# if GPA is over 3.0 and age is over 16, accept

if GPA > 3.0 and age > 16:
	print("Congrats, you have been accepted to Stanford!")
else:
	print("Sorry, you'll have to go Harvard instead")
