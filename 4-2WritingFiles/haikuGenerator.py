# make a welcom statment
print("Welcome to the Haiku Generator! Lets make a haiku!")
# make  a list that stores the stanzas
poemList = []
# make a questionare that asks the user for each line and appends it to poemList
print("Provide the first line:")
line1  = raw_input()
poemList.append(line1)
print("Provide the second line:")
line2 = raw_input()
poemList.append(line2)
print("Provide the third line:")
line3 = raw_input()
poemList.append(line3)
# ask the user what they would like
print("What would you like to call the file you put your haiku in to? *REMEMBER: every file has to have no spaces and must be followed by .txt*")
haikuPoem = raw_input()
file = open(haikuPoem , 'a')
# make a loop that appends each line to the bottem of the file
for list in poemList:
	file.write(list + "\n")
# make a congratulations message that tells the user how to view their poem
print("Congratulation! To see your haiku just type cat with a space along with your file name!")
