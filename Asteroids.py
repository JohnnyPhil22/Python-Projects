import turtle, math, random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Asteroids!")
wn.setup(800, 600)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)


class Sprite:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        self.active = True

    def update(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy

            if self.x > 400:
                self.x = -400
            elif self.x < -400:
                self.x = 400

            if self.y > 300:
                self.y = -300
            elif self.y < -300:
                self.y = 300

    def render(self, pen):
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size, self.size, 0)
            pen.color(self.color)
            pen.stamp()

    def is_collision(self, other):
        x = self.x - other.x
        y = self.y - other.y
        distance = ((x**2) + (y**2)) ** 0.5
        if distance < ((10 * self.size) + (10 * other.size)):
            return True
        else:
            return False

    def goto(self, x, y):
        self.x = x
        self.y = y


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "triangle"
        self.lives = 3
        self.score = 0

    def rotate_left(self):
        self.heading += 30

    def rotate_right(self):
        self.heading -= 30

    def accelerate(self):
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx += ax * 0.1
        self.dy += ay * 0.1

    def decelerate(self):
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx -= ax * 0.1
        self.dy -= ay * 0.1

    def render(self, pen):
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size / 2.0, self.size, 0)
            pen.color(self.color)
            pen.stamp()


class Asteroid(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "circle"


class Missile(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "circle"
        self.size = 0.2
        self.active = False

    def update(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy

            if self.x > 400:
                self.active = False
            elif self.x < -400:
                self.active = False

            if self.y > 300:
                self.active = False
            elif self.y < -300:
                self.active = False

    def fire(self):
        if not self.active:
            self.active = True
            self.x = player.x
            self.y = player.y
            self.heading = player.heading
            self.dx = math.cos(math.radians(self.heading)) * 1
            self.dy = math.sin(math.radians(self.heading)) * 1


sprites = []

player = Player()
sprites.append(player)

missile = Missile()
sprites.append(missile)

for _ in range(5):
    asteroid = Asteroid()
    x = random.randint(-375, 375)
    y = random.randint(-275, 275)
    asteroid.goto(x, y)
    dx = random.randint(-5, 5) / 20.0
    dy = random.randint(-5, 5) / 20.0
    asteroid.dx = dx
    asteroid.dy = dy
    size = random.randint(10, 30) / 10.0
    asteroid.size = size
    sprites.append(asteroid)

wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeypress(player.decelerate, "Down")
wn.onkeypress(missile.fire, "space")

while True:
    pen.goto(-350, 250)
    pen.write(f"{player.score}", False, font=("commodore 64 pixelized", 18, "normal"))

    pen.clear()

    for i in range(player.lives):
        pen.goto(-350 + 30 * i, 225)
        pen.shape("triangle")
        pen.shapesize(0.7, 0.7, 0)
        pen.setheading(90)
        pen.stamp()

    for sprite in sprites:
        sprite.update()
        sprite.render(pen)

    for sprite in sprites:
        if isinstance(sprite, Asteroid):
            if player.is_collision(sprite):
                player.lives -= 1
                player.goto(0, 0)
                sprite.goto(100, 100)

                if player.lives <= 0:
                    player.active = False

            if player.lives == 0:
                wn.bye()

            if missile.active and missile.is_collision(sprite):
                missile.active = False
                player.score += 10
                sprite.goto(100, 100)

wn.mainloop()
