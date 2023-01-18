from turtle import *

title('Turtle Star')
bgcolor('black')
color('red','red')

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

hideturtle()

mainloop()