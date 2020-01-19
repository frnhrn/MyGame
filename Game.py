# Let's create a simple Snake Game in Python 3
# By Florian H.

import turtle
import time

delay = 0.1

# Set up the screen

window = turtle.Screen()
window.title("Snake Game By Florian H.")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0) #turn off the screen updates



#Snake Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup() #so that it will not draw anything when the turtule is moving
head.goto(0,0) #when the head start we want it to be in the center of the screen so yaxe and xaxe are 0
head.direction = "stop"


# My Functions

def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

#Head Directions

def move():
    if head.direction == "up":
        yaxe = head.ycor()
        head.sety(yaxe + 20)

    if head.direction == "down":
        yaxe = head.ycor()
        head.sety(yaxe - 20)

    if head.direction == "left":
        xaxe = head.xcor()
        head.setx(xaxe - 20)

    if head.direction == "right":
        xaxe = head.xcor()
        head.setx(xaxe + 20)

#Keyboard bindings (connect Key press to a particular function)

window.listen()
window.onkeypress(go_up, "z")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "q")
window.onkeypress(go_right, "d")


#Main game loop

while True:
    window.update()

    move()

    time.sleep(delay)


window.mainloop()