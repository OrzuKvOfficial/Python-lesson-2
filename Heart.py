import turtle

def draw_heart():
    t = turtle.Turtle()
    t.color('blue')
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.setheading(60)
    t.circle(-90, 200)
    t.forward(100)
    t.end_fill()
    t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("black")

draw_heart()

turtle.done()
