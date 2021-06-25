import turtle as t
import math 


harsh = t.Turtle()
harsh.color('pink','red')



harsh.speed(0)

def line_1():
    for i in range(400):
        harsh.forward(5)
        harsh.right(math.sin(i/20)*30)
        harsh.left(math.tan(i/50)*40)
        harsh.forward(5)
        harsh.left(math.cos(i/10)*20)
        harsh.forward(1)

line_1()

harsh.hideturtle()

t.done()
