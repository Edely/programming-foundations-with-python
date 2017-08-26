import turtle

def draw_screen():
	window = turtle.Screen()
	window.bgcolor("blue")

	draw_square()
	draw_circle()
	draw_triangle()

	window.exitonclick()

def draw_square():
	brad = turtle.Turtle()
	brad.shape("turtle")	
	brad.speed(1)
	brad.color("red")

	turn = 0
	while turn < 4:
		brad.forward(100)
		brad.right(90)
		turn = turn + 1

def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("yellow")
	angie.circle(100)

def draw_triangle():
	bob = turtle.Turtle()
	bob.shape("circle")
	bob.color("white")

	turn = 0
	while turn < 3:
		bob.forward(70)
		bob.left(120)

		turn = turn + 1


draw_screen()
