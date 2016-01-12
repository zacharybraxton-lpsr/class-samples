
current_GPA = 1.4

# eligibility to play basketball
eligible_to_play_GPA = 2.5
 
while current_GPA < eligible_to_play_GPA:
  print("Study harder!")
  boost = raw_input("Did your GPA go up or down during the loop") 
  if  boost == "up":
	 current_GPA = current_GPA  + .1
	 print("Your GPA is now " + str(current_GPA) + " and you're" + str(eligible_to_play_GPA - current_GPA) + " away from being able to play")

  elif boost == "down":
        current_GPA = current_GPA - .1
        print("Your GPA is now " + str(current_GPA) + " and you're" + str(eligible_to_play_GPA - current_GPA) + " away from being able to play")
	

  
