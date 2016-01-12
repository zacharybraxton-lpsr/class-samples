import turtle
from Tkinter import *
import random
chroma = ['red','blue','green','yellow']
#make shapes
def square(myTurtle):
	blip = 0
	while blip < 4:
		 myTurtle.forward(100)
		 myTurtle.left(90)
		 blip = blip + 1
def triangle(myTurtle):
	blip2 = 0
	while blip2 < 3:
		myTurtle.forward(100)
		myTurtle.left(120)
		blip2 = blip2 + 1
def octagon(myTurtle):
	blip3 = 0
	while blip3 < 8:
		myTurtle.forward(100)
		myTurtle.left(45)
		blip3 = blip3 + 1
# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)
# create our turtle
shawn = turtle.Turtle()
# make some simple buttons
fwd = Button(frame, text ='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text ='left', command=lambda: shawn.left(90))
right = Button(frame, text = 'right', command =lambda: shawn.right(90))
penup = Button(frame, text = 'pen up', command=lambda: shawn.penup())
pendown= Button(frame, text = 'pen down', command=lambda: shawn.pendown())
color = Button(frame, text = 'random  color', command=lambda: shawn.color(random.choice(chroma)))
polygon1 = Button(frame, text = 'square', command=lambda: square(shawn))
polygon2 = Button(frame, text = 'triangle', command=lambda: triangle(shawn))
polygon3 = Button(frame, text = 'octagon', command=lambda: octagon(shawn))
redo = Button(frame, text = 'redo',command=lambda: shawn.goto(0,0)
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
color.pack(side=LEFT)
polygon1.pack(side=LEFT)
polygon2.pack(side=LEFT)
polygon3.pack(side=LEFT)
redo.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
