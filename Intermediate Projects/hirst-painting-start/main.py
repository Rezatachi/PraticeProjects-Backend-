###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract(
#     'Intermediate Projects\hirst-painting-start\dots.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


import turtle as turtle_module
import random

# Change its colormode to 255
turtle_module.colormode(255)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110),
              (240, 245, 241), (236, 239, 243), (149, 75, 50)]

tim = turtle_module.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
tim.dot(20, random.choice(color_list))
for dot_count in range(1, num_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)

        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
