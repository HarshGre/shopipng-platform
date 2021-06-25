import turtle
import math


harsh=turtle.Turtle()
harsh.speed(0)
harsh.color('cyan')

for i in range(2000):
    harsh.forward(10)
    harsh.left(math.sin(i/10)*25)
    harsh.left(20)


harsh.hideturtle()

turtle.done()