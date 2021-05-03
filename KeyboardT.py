import turtle
import random


def up():
    turtle.setheading(90)
    turtle.forward(100)

def down():
    turtle.setheading(270)
    turtle.forward(100)

def left():
    turtle.setheading(180)
    turtle.forward(100)

def right():
    turtle.setheading(0)
    turtle.forward(100)

colors = ["red", "blue", "green", "yellow", "black"]

def clickLeft(x, y):  # Make sure to have parameters x, y
    turtle.color(random.choice(colors))

def clickRight(x, y):
    turtle.stamp()




turtle.listen()

turtle.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRight, 3) # 3: Right Mouse Button

turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()  # This will make sure the program continues to run 