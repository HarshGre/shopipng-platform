import turtle
import math


harsh=turtle.Turtle()
harsh.speed(0)


for i in range(2000):
    harsh.forward(math.sqrt(i))
    harsh.left(i%180)


harsh.hideturtle()

turtle.done()