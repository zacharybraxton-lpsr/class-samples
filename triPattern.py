import turtle

def bowTie(turtle):
	trip = 0
	while trip < 3:
		triDown(turtle)
                turtle.left(180)
                turtle.penup()
                turtle.forward(125)
                turtle.right(180)
                turtle.pendown()
                turtle.left(30)
                trip = trip + 1
def bowTie2(turtle):
	trip2 = 0
	turtle.left(90)
	while trip2 < 3:
		 triangle(turtle)
                 turtle.left(180)
                 turtle.penup()
                 turtle.forward(125)
                 turtle.right(180)
                 turtle.pendown()
                 turtle.left(30)
                 trip2 = trip2 + 1



def triangle(turtle):
	blip = 0
	while blip < 4:
		turtle.forward(10)
		turtle.left(120)
		turtle.forward(10)
                turtle.left(120)
		turtle.forward(10)
                turtle.left(120)
		turtle.penup()
		turtle.forward(30)
		turtle.pendown()
		blip = blip + 1
def triDown(turtle):
        blip2 = 0
        while blip2 < 4:
		turtle.forward(10)
                turtle.right(120)
                turtle.forward(10)
                turtle.right(120)
                turtle.forward(10)
                turtle.right(120)
                turtle.penup()
                turtle.forward(30)
                turtle.pendown()
                blip2 = blip2 + 1


		


shawn = turtle.Turtle()
bowTie(shawn)
bowTie2(shawn)
turtle.exitonclick()
