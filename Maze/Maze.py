import turtle, math, random

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Maze")
wn.setup(700,700)
wn.tracer(0)

# Register images/shapes
images = ["Python-Projects\Maze\wizard_right.gif", "Python-Projects\Maze\wizard_left.gif", "Python-Projects\Maze\gold_chest.gif", "Python-Projects\Maze\wall.gif", "Python-Projects\Maze\enemy_right.gif", "Python-Projects\Maze\enemy_left.gif"]
for image in images:
    turtle.register_shape(image)

# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("Python-Projects\Maze\wizard_right.gif")
        self.color("blue")
        self.penup()
        self.lives = 3
        self.no_lives = 0
        self.speed(0)
        self.gold = 0
        self.max_gold = 500
    
    def go_up(self):
        # Calculate spot to move player
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # Check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    
    def go_down(self):
        # Calculate spot to move player
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate spot to move player
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("Python-Projects\Maze\wizard_left.gif")

        # Check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate spot to move player
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape("Python-Projects\Maze\wizard_right.gif")

        # Check if space has wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a=self.xcor()-other.xcor()
        b=self.ycor()-other.ycor()
        distance=math.sqrt((a**2)+(b**2))

        if distance<5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Python-Projects\Maze\gold_chest.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Python-Projects\Maze\enemy_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction=random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("Python-Projects\Maze\enemy_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("Python-Projects\Maze\enemy_right.gif")
        else:
            dx = 0
            dy = 0
        
        # Check if player is nearby
        # If yes, go there
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction="left"
            elif player.xcor() > self.xcor():
                self.direction="right"
            elif player.ycor() < self.ycor():
                self.direction="down"
            elif player.ycor() > self.ycor():
                self.direction="up"

        # Calculate spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if space has a wall
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            # Choose different direction
            self.direction=random.choice(["up","down","left","right"])
        
        # Set timer to move next time
        turtle.ontimer(self.move,t=random.randint(100,300))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+(b**2))
        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
    
# Create levels list
levels = [""]

# Define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXXE          XXXXX",
    "X  XXXXXXX  XXXXXXX  XXXXX",
    "X       XX  XXXXXXX  XXXXX",
    "X       XX  XXXX       EXX",
    "XXXXXX  XX  XXXX        XX",
    "XXXXXX  XX  XXXXXXX  XXXXX",
    "XXXXXX  XX     XXXX  XXXXX",
    "X  XXX         XXXX TXXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXXX",
    "X              TXXXXXXXXXX",
    "X               XXXXXXXXXX",
    "XXXX XXXXXXX    XXXXXXX  X",
    "XXXE TXXXXXXXX  XXXXXXX  X",
    "XXXXXXXXXXXXXX           X",
    "XXXE                     X",
    "XXX        XXXXXXXXXXXXXXX",
    "XXXXXXXXXETXXXXXXXXXXXXXXX",
    "XXXXXXXXX                X",
    "XX  XXXXX                X",
    "XX TXXXXXXXXXXXXXX   XXXXX",
    "XXT  YXXXXXXXXXXXX   XXXXX",
    "XXXXE                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Create treasures list
treasures = []

# Create enemies list
enemies = []

# Add maze to mazes list
levels.append(level_1)

# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range (len(level[y])):

            # Get character at each x and y coordinate
            # Note the order of y and x in the next line
            character = level[y][x]
            
            # Calculate screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("Python-Projects\Maze\wall.gif")
                pen.stamp()
                # Add coordinates to wall
                walls.append((screen_x, screen_y))
            
            # Check if it is a P (player)
            if character == "P":
                player.goto(screen_x, screen_y)

            # Check if it is a T (treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            
            # Check if it is an E (treasure)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Set up level
setup_maze(levels[1])

# Keyboard Bindings
wn.listen()
wn.onkey(player.go_down, "Down")
wn.onkey(player.go_left, "Left")
wn.onkey(player.go_right, "Right")
wn.onkey(player.go_up, "Up")

wn.tracer(0)

# Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)

# Main Game Loop
while True:
    # Check for player collision with treasure
    # Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):

            # Add treasure gold to player gold
            player.gold += treasure.gold
            print(f"Player Gold: {player.gold}")
            
            # Destroy treasure
            treasure.destroy()

            # Remove treasure from treasures list
            treasures.remove(treasure)
    
    for enemy in enemies:
        if player.is_collision(enemy):
            player.gold-=50
            print(f"Player Gold: {player.gold}")
            player.lives-=1
            print(f"Player Lives: {player.lives}")
            if player.lives==player.no_lives:
                print(f"Player Gold: {player.gold}")
                wn.bye()
     
    # Update Screen
    wn.update()

wn.mainloop()