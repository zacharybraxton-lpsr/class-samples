# define a classs called Player
class Player(object):
# make __init__ variable that sets up player class
  def __init__(self,name,age,goals):
    self.name = name
    self.age = age
    self.goals = goals
# make a prinStats variable that sets up the player profile
  def printStats(self):
    print("Name: " + self.name)
    print("Age: " + str(self.age))
    print("Goals: " + str(self.goals))
    print(" ")
# make a welcome interface that displyas user options
print("Welcome to the Soccer Team Management Program! What action would you like to do ?")
print("(1) Add a new player")
print("(2) Print your roster")
print("(3) Team's age average")
print("(4) Team's goal average")
print("(5) Exit the program")
# make a team data storage list

# set up an user input variable for player and average
user_choice = int(raw_input())
playRoster = []
counter1 = 0
counter2 = 0
age = 0
goals = 0
# make a loop that keeps asking the user what they would like to do
while user_choice != (5):
# if statement that starts up process for creating a profile  
  if user_choice == 1:
    print("What's your player's name?")
    playName = raw_input()
    print("What's your player's age?")
    playAge = int(raw_input())
    print("What's your player's number of goals?")
    playGoals = int(raw_input())
    playRoster.append(Player(playName,playAge,playGoals))  
    counter1 = counter1 + 1
    counter2 = counter2 + 1
    age = age + playAge
    goals  = goals + playGoals
    print("What would you like to do now?")
    user_choice = int(raw_input())

# make an elif statement that prints the roster  
  elif user_choice == 2:
    for g in playRoster:
      g.printStats()
    print("What would you like to do now?")
    user_choice = int(raw_input())
# make an elif statement that finds the average age and prints it
  elif user_choice == 3:
    avg1 = str(age / counter1)
    print("Team age average: " + avg1)
    print("What would you like to do now?")
    user_choice = int(raw_input())
# make an elif statement that finds the average goals and prints it
  elif user_choice == 4:
    avg2 = str(goals / counter2)
    print("Team goal average: " + avg2)
    print("What would you like to do now?")
    user_choice = int(raw_input())
		
