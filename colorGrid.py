import turtle
# blue green yellow red
def colorStick(turtle):
        section = 0
        while section < 50 :
                multiSquare(turtle)
                turtle.right(90)
                turtle.penup()
		turtle.forward (35)
                turtle.left(90)
                turtle.forward(20)
		turtle.pendown()
		section = section + 1


def multiSquare(turtle):
	turtle.color('blue')
	square(turtle)
	turtle.right(90)
	turtle.color('green')
	square(turtle)
	turtle.right(90)
	turtle.color('yellow')
        square(turtle)
        turtle.right(90)
	turtle.color('red')
        square(turtle)
        turtle.right(90)

def square(turtle):
	angle = 0
	while angle < 4:
		turtle.forward(10)
		turtle.left(90)
		angle = angle + 1
	
shawn = turtle.Turtle()
shawn.shape('turtle')
shawn.speed(0)
colorStick(shawn)
turtle.exitonclick()
