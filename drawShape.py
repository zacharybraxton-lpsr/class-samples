import turtle

def drawSide(myTurtle):
	count = 0
	while count < 16:
		drawVee(myTurtle)
		count = count + 1
		if count % 4 == 0:
			myTurtle.right(90)
			myTurtle.forward(20)
			myTurtle.right(90)
def drawVee(myTurtle):
	myTurtle.forward(20)
	myTurtle.right(90)
	myTurtle.forward(20)
	myTurtle.left(90)
shawn = turtle.Turtle()
drawSide(shawn)

turtle.exitonclick()
