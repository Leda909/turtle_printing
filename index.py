import turtle
tina = turtle.Turtle()
tina.shape('turtle')

your_name = input("What's your name?")

tina.penup()
tina.goto(0,150)
tina.write("Hello, " + your_name + "!")
tina.goto(0,100)
tina.write("I do not draw when my pen is up!")
tina.goto(0,50)

tina.pendown()
tina.color("blue")
tina.write("I do draw when my pen is down!")
tina.goto(-100,50)

tina.color("purple")
tina.goto(-100,-50)

tina.color("green")
tina.goto(0,-50)

tina.color("orange")
tina.goto(0,50)
