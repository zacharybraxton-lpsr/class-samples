import turtle
def rhombus1(turtle):
  blip = 0
  turtle.right(60)
  turtle.fillcolor("light blue")
  while blip < 2:
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(60)
    turtle.forward(40)
    turtle.left(120)
    turtle.end_fill()
    blip = blip + 1
  turtle.right(30)

def rhombus2(turtle):
  blip2 = 0
  turtle.left(90)
  turtle.fillcolor("red")
  while blip2 < 2:
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(60)
    turtle.forward(40)
    turtle.left(120)
    turtle.end_fill()
    blip2 = blip2 + 1

def rhombus3(turtle):
  blip3 = 0
  turtle.left(30)
  while blip3 < 2:
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(60)
    blip3 = blip3 + 1
  turtle.right(120)
  turtle.forward(40)
  turtle.left(90)
  
def cube(turtle):
  rhombus3(turtle)
  rhombus2(turtle)
  rhombus1(turtle)

def cubePattern(turtle):
  corner = 0
  while corner < 3:
    cube(turtle)
    turtle.penup()
    turtle.right(30)
    turtle.forward(40)
    turtle.left(30)
    turtle.pendown()
    corner = corner + 1
def cubeRow(turtle):
  row  = 0
  while row < 10:
    cubePattern(turtle)
    turtle.penup()
    turtle.left(150)
    turtle.forward(40)
    turtle.right(30)
    turtle.forward(208)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(210)
    turtle.pendown()  
    row = row + 1

shawn = turtle.Turtle()
shawn.speed(0)
cubeRow(shawn)
turtle.exitonclick()
