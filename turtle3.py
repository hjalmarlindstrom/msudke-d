import turtle
def waves(repeats = 1):
    """Draws nested colored sinusoids emerging from darkness"""
    for i in range(repeats):
        alex.up()
        alex.color(hueGen(i, .5*i/repeats, .5))
        alex.goto(-315,315 - i)
        alex.seth(45) # set heading
        x = alex.xcor()
        y = alex.ycor()
        f = i + 1
        for j in range(630):
            x = alex.xcor()
            alex.goto(x + 1, y + 25*sin(8*j/f + i/25)) # plot sines
            alex.down()
            x = alex.xcor()
turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(1)
turtle.bgcolor("black")
alex = turtle.Turtle()
alex.speed(10)
alex.pensize(2)
alex.ht()
waves(700)
turtle.update()
wn.exitonclick()
