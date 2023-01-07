import turtle
import random
import randomcolor

t = turtle.Turtle()

starsNumber = 5

def draw_star(x, y, multiplier, color):
    t.penup()
    t.goto(x, y)
    t.right(random.randrange(-180, 180))
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.right(75)
    t.forward(100 * multiplier)
    
    for _ in range(4):
        t.right(144)
        t.forward(100 * multiplier)
    t.end_fill()
    t.penup()

for _ in range(starsNumber):
    x = random.randrange(-350, 350)
    y = random.randrange(-350, 350)
    multiplier = random.uniform(0.3,3)
    color = randomcolor.RandomColor().generate()
    draw_star(x, y, multiplier, color[0])

turtle.hideturtle()
turtle.done()