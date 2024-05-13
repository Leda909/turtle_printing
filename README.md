# Draw in Python with turtle

![image](https://github.com/Leda909/turtle_python/assets/65784743/9e97d8a7-07a4-4325-84c1-88897b6dc243)

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

![image](https://github.com/Leda909/turtle_python/assets/65784743/4b551f91-be32-4c66-81b4-d4e52ea78a19)

import turtle
tina = turtle.Turtle()
tina.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

for each_color in colors:
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.circle(40)
    tina.right(angle)
    tina.forward(30)

turtle.done()

![image](https://github.com/Leda909/turtle_python/assets/65784743/cac192f5-c531-4c01-b931-42906e358e37)

![image](https://github.com/Leda909/turtle_printing/assets/65784743/f67e19e8-5881-4fcc-b054-a221a182e0e6)
