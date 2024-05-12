import turtle
tina = turtle.Turtle()
tina.shape('turtle')

#Drawn face
tina.penup()
tina.begin_fill()
tina.color('pink')
tina.goto(30,-150)
tina.pendown()
tina.circle(130)
tina.penup()
tina.end_fill()

# Draw right eye
tina.color('white')
tina.goto(0,0)
tina.begin_fill()
tina.pendown()
tina.circle(20)
tina.penup()
tina.end_fill()
tina.begin_fill()

# Draw left pupil
tina.color('black')
tina.pendown()
tina.circle(10)
tina.penup()
tina.end_fill()
tina.forward(60)
tina.right(45)
tina.begin_fill()

# Draw right eye
tina.color('white')
tina.pendown()
tina.circle(30)
tina.penup()
tina.end_fill()

# Draw right pupil
tina.begin_fill()
tina.color('black')
tina.pendown()
tina.circle(10)
tina.penup()
tina.end_fill()

#Draw mounth
tina.begin_fill()
tina.color('red')
tina.goto(-20, -50)
tina.pendown()
tina.right(70)
tina.circle(40, 220)
tina.goto(-20, -50)
tina.penup()
tina.end_fill()

turtle.done()