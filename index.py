import turtle

tina = turtle.Turtle()
tina.shape('turtle')
tina.speed(3)  # Set the speed

color_list = ["red", "blue", "green", "orange", "purple", "yellow"]

# Draw a triangle with a given color
def draw_triangle(color):
    tina.color(color)  # Set the color of the triangle
    tina.begin_fill()  # Start filling the triangle
    for _ in range(3):
        tina.forward(30)
        tina.left(120)
    tina.end_fill()  # End filling the triangle

# Draw a hexagon composed of triangles, each with a different color
for i, color in enumerate(color_list):
    tina.penup()
    tina.goto(0, 0)  # Go back to the center of the circle
    tina.setheading(60 * i)  # Set the heading for the next triangle
    tina.pendown()
    draw_triangle(color)

turtle.done()
