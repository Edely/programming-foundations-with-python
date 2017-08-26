import turtle

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("blue")

	brad = turtle.Turtle()
	brad.shape("turtle")	
	brad.speed(2)
	brad.color("red")
	for i in range(1, 37):
		draw_square(brad)
		brad.right(10)

	window.exitonclick()


#def draw_circle():
#	angie = turtle.Turtle()
#	angie.shape("arrow")
#	angie.color("yellow")
#	angie.circle(100)



draw_art()
