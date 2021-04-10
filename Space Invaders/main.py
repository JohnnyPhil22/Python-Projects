import turtle
import os
import math
import random
import platform

if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module not available.")

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by Jonathan")
wn.setup(width=800, height=800)
wn.bgpic("space_invaders_background.gif")
wn.tracer(0)

# Register shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set score to 0
score = 0

# Draw score on screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(-290, 270)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.speed = 0

# Create enemy
number_of_enemies = 55

enemies = []

# Add enemies to list
for i in range(number_of_enemies):
    # Create enemies
    enemies.append(turtle.Turtle())

enemy_start_x = -275
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.goto(x, y)
    # Update enemy number
    enemy_number += 1
    if enemy_number == 11:
        enemy_start_y -= 50
        enemy_number = 0

    enemyspeed = 0.2

# Create bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 1.4

# Define bullet state
bulletstate = "ready"

# Move the player left
def move_left():
    player.speed = -0.6

# Move the player right
def move_right():
    player.speed = 0.6

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

# Make bullet move
def fire_bullet():
    # Make bulletstate global
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move bullet just above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        play_sound("laser.wav")

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

def play_sound(sound_file, time=0):
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    
    # Repeat sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time, t = int(time * 1000)))

# Play BGM
play_sound("space_invaders_bgm.wav", 119)

# Keyboard Bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")

# Main Game Loop
while True:
    wn.update()
    move_player()
    for enemy in enemies:
        # Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1
        
        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        # Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            # Reset bullet
            bullet.hideturtle()
            bullet.bulletstate = "ready"
            bullet.setposition(0, -400)
            
            # Reset enemy
            enemy.goto(0, 10000)
            
            # Update score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

            # Play sound
            play_sound("explosion.wav")

        # Check for collision between player and enemy
        if isCollision(player, enemy):
            play_sound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over.")
            break

    # Move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check if bullet has gone to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

wn.mainloop()
