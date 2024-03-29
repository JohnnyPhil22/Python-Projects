import turtle
from utils import square, vector

turtle.setup(420, 420, 370, 0)
turtle.title('TRON')
turtle.bgcolor('black')
turtle.hideturtle()
turtle.tracer(False)

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()


def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200


def draw():
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if p1head in p1body or p1head in p2body:
        turtle.clear()
        turtle.penup()
        turtle.goto(-65, 0)
        turtle.pendown()
        turtle.color('cyan')
        turtle.write('Cyan wins!', font=('Arial', 20))
        return
    
    if p2head in p2body or p2head in p1body:
        turtle.clear()
        turtle.penup()
        turtle.goto(-80, 0)
        turtle.pendown()
        turtle.color('orange')
        turtle.write("Orange wins!", font=('Arial', 20))
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'orange')
    square(p2xy.x, p2xy.y, 3, 'cyan')
    turtle.update()
    turtle.ontimer(draw, 50)


turtle.listen()
turtle.onkey(lambda: p1aim.rotate(90), 'a')
turtle.onkey(lambda: p1aim.rotate(-90), 'd')
turtle.onkey(lambda: p2aim.rotate(90), 'Right')
turtle.onkey(lambda: p2aim.rotate(-90), 'Left')

draw()

turtle.mainloop()
