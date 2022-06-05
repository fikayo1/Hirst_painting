import colorgram
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()

# TO EXTACT THE COLORS FROM THE PICTURE
# colors = colorgram.extract('C://Users//Sammy//Documents//python angela//Day_18//image.jpg', 30)
# # end = []
# # for i in range(len(color)):
# #     first_color = color[i]
# #     rgb = first_color.rgb
# #     print(rgb)
# #     end += rgb
# # print(tuple(end))
# rbg_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rbg_color.append(new_color)
# print(rbg_color)

def drawdots():
    for i in range(10):
        tim.dot(20, random.choice(clor_list))
        tim.penup()
        tim.forward(50)
clor_list = [ (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.speed(0)

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(10):
    drawdots()
        
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


 



screen = Screen()
screen.exitonclick()