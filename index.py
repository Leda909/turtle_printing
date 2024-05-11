import turtle
tina = turtle.Turtle()
tina.shape('turtle')

your_name = input("What's your name?")

tina.penup()
tina.left(90)
tina.forward(30)
tina.color("blue")
tina.write("Hello, " + your_name + "!")
tina.write("What color am I now?")

tina.forward(30)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(30)
tina.color("green")
tina.write("What color am I now?")