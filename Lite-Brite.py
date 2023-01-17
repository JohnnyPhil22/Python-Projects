import turtle

WIDTH = 985
HEIGHT = 170

wn = turtle.Screen()
wn.title("Lite-Brite Simulator by Jonathan")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)

color_codes = {"r":"red"," ":"black"}

pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.shape("circle")

def draw_circle(x, y, pen):
    screen_x = -(WIDTH/2.0) + 20 + x * 20
    screen_y = (HEIGHT/2.0) - 20 - y * 20
    pen.goto(screen_x, screen_y)
    pen.stamp()
picture = [
"rrrrr rrrrr rrrrr rrrrr       rrrrr rrrrr rrrrr",
"  r   r   r     r     r       r   r r   r     r",
"  r   r   r     r     r       r   r r   r     r",
"  r   rrrrr rrrrr rrrrr       r   r r   r    r ",
"r r   r     r     r           r   r r   r   r  ",
"r r   r     r     r           r   r r   r  r   ",
"rrr   r     rrrrr rrrrr rrrrr rrrrr rrrrr r    ",
]

# Draw picture
for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x, y, pen)
    
wn.mainloop()
