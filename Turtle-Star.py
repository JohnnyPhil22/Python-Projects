from turtle import *

title("Turtle Star")
bgcolor("black")

f = "r"

while True:
    if f == "r":
        color("red")
        forward(200)
        left(170)
        if abs(pos()) < 1:
            f = "w"
    if f == "w":
        color("white")
        forward(200)
        left(170)
        if abs(pos()) < 1:
            f = "r"

mainloop()
