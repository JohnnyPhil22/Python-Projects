import turtle, winsound

wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
Score_A = 0
Score_B = 0

# Paddle A
Paddle_A = turtle.Turtle()
Paddle_A.speed(0)
Paddle_A.shape("square")
Paddle_A.color("white")
Paddle_A.shapesize(stretch_wid=5, stretch_len=1)
Paddle_A.penup()
Paddle_A.goto(-350, 0)

# Paddle B
Paddle_B = turtle.Turtle()
Paddle_B.speed(0)
Paddle_B.shape("square")
Paddle_B.color("white")
Paddle_B.shapesize(stretch_wid=5, stretch_len=1)
Paddle_B.penup()
Paddle_B.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.1
Ball.dy = -0.1

# Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 230)
Pen.write("Player 1: 0    Player 2: 0", align="center", font=("Courier", 24, "bold"))

# Net
Net = turtle.Turtle()
Net.speed(0)
Net.color("white")
Net.penup()
Net.hideturtle()
Net.goto(0, 400)
Net.pendown()
for _ in range(600):
    Net.fd(20)
    Net.penup()

# Functions
def Paddle_A_up():
    y = Paddle_A.ycor()
    y += 20
    Paddle_A.sety(y)
def Paddle_A_down():
    y = Paddle_A.ycor()
    y -= 20
    Paddle_A.sety(y)
def Paddle_B_up():
    y = Paddle_B.ycor()
    y += 20
    Paddle_B.sety(y)
def Paddle_B_down():
    y = Paddle_B.ycor()
    y -= 20
    Paddle_B.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(Paddle_A_up, "w")
wn.onkeypress(Paddle_A_down, "s")
wn.onkeypress(Paddle_B_up, "Up")
wn.onkeypress(Paddle_B_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border-Checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("Pong\Bounce.wav", winsound.SND_ASYNC)
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("Pong\Bounce.wav", winsound.SND_ASYNC)
    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_A += 1
        winsound.PlaySound("Pong\Cheer.wav", winsound.SND_ASYNC)
        Pen.clear()
        Pen.write("Player 1: {}    Player 2: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "bold"))
    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_B += 1
        winsound.PlaySound("Pong\Cheer.wav", winsound.SND_ASYNC)
        Pen.clear()
        Pen.write("Player 1: {}    Player 2: {}".format(Score_A, Score_B), align="center", font=("Courier", 24, "bold"))

    # Paddle and Ball Collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Paddle_B.ycor() + 40 and Ball.ycor() > Paddle_B.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound("Pong\Bounce.wav", winsound.SND_ASYNC)
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Paddle_A.ycor() + 40 and Ball.ycor() > Paddle_A.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1
        winsound.PlaySound("Pong\Bounce.wav", winsound.SND_ASYNC)

wn.mainloop()