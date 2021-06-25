import turtle
import math


harsh=turtle.Turtle()

harsh.speed(0)

harsh.penup()
harsh.goto(-200,200)
harsh.pendown()
harsh.color('cyan','green')

a=0
b=0

while True:
    harsh.forward(a)
    harsh.right(b)
    a+=2
    b+=1
    if a==40 or b==10:
        harsh.forward(a)
        harsh.left(b)
        a-=1
        b-=1
        if a==50:
            break



harsh.hideturtle



turtle.done()