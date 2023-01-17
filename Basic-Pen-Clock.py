import turtle, time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock")
wn.tracer(0)

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):
    # Draw clock face
    pen.up()        
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # Draw 12 hour-lines of the clock
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    # Draw hour hand
    pen.penup()
    pen.goto(0,0)    
    pen.color("red")
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(75)

    # Draw minute hand
    pen.penup()
    pen.goto(0,0)    
    pen.color("blue")
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(175)

    # Draw seconds hand
    pen.penup()
    pen.goto(0,0)    
    pen.color("yellow")
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    
    draw_clock(h, m, s, pen)
    wn.update()
    pen.clear()

wn.mainloop()
