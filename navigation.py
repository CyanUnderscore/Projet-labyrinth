import turtle 

speed = 10
turtle.up()
def gauche(): 
	turtle.goto(turtle.xcor()-speed, turtle.ycor())
	turtle.setheading(180)
def droite(): 
	turtle.goto(turtle.xcor()+speed, turtle.ycor())
	turtle.setheading(0)
def bas(): 
	turtle.goto(turtle.xcor(), turtle.ycor()-speed)
	turtle.setheading(270)
def haut(): 
	turtle.goto(turtle.xcor(), turtle.ycor()+speed)
	turtle.setheading(90)

# key bindings
turtle.onkeypress(gauche,"Left")
turtle.onkeypress(droite,"Right")
turtle.onkeypress(haut,"Up")
turtle.onkeypress(bas,"Down")
turtle.listen()

# start loop
turtle.goto(0,0)
turtle.mainloop()