print("What is your favorite number?")
number = int(input())

while number > 14:
    print("I don’t like that number - try another!")
    if number == 14:
        print("You have chosen the best number!")
    else:
        print("I don't like that number - try another!")
