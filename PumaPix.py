print("Welcome to PumaPix! Let's set up your que.")
print("What are your favorite shows?")
print("When you are finished, type 'save'")
show = raw_input()
showX = []
while show != "save":
	print("Enter a show name:")
	show = raw_input()
	if show  == "save":
		print("Cool! Your current shows are:")
		
		for showY in showX:
			print(showY)
		print("Now we are going to scroll through your list to see if you selected one of our 'lesser' titles.") 	
		showX.append("Breaking Bad")
		showX.append("Criminal Minds")
		print("We scanned your titles, and added some good ones. Enjoy your new que! ") 
		showX.sort()
		num = 1
		for showZ in showX :
			print(str(num)+ "." + showZ)
			num = num + 1
	else:		
		showX.append(show)
