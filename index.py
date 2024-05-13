import turtle

tina = turtle.Turtle()
tina.shape('turtle')

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
color_list = ["blue", "purple", "green"]

for color in color_list:
    tina.color(color)
    tina.write(color)
    for number in number_list:
        tina.forward(number * 10)
        tina.left(60)

turtle.done()
