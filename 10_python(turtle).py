import turtle



harsh=turtle.Turtle()
harsh.color('red','yellow')
harsh.speed(0)



harsh.begin_fill()
for i in range(100):
    harsh.forward(300)
    harsh.left(170)

harsh.end_fill()

harsh.hideturtle()

turtle.done()