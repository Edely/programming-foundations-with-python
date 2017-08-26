import turtle

def draw_screen():
	window = turtle.Screen()
	window.bgcolor("yellow")
	window.screensize(700, 700)

	linus = turtle.Turtle()
	linus.color("pink")
	linus.speed(10)
	linus.shape("classic")

	for i in range(1, 37):
		draw_petal(linus)
		linus.left(10)

	linus.right(90)
	linus.forward(350)


	window.exitonclick()


def draw_petal(some_turtle):
	some_turtle.forward(100)
	some_turtle.left(40)
	some_turtle.forward(100)
	some_turtle.left(140)
	some_turtle.forward(100)
	some_turtle.left(40)
	some_turtle.forward(100)


draw_screen()