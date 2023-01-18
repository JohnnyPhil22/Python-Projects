import turtle

WIDTH,HEIGHT=970,170

wn = turtle.Screen()
wn.title("Lite-Brite")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)
wn.tracer(0)

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
"rrrrr rrrrr r   r rrrrr rrrrr r   r rrrrr r   r",
"  r   r   r r   r r   r   r   r   r r   r r   r",
"  r   r   r rr  r r   r   r   r   r r   r rr  r",
"  r   r   r r r r rrrrr   r   rrrrr rrrrr r r r",
"r r   r   r r  rr r   r   r   r   r r   r r  rr",
"r r   r   r r   r r   r   r   r   r r   r r   r",
"rrr   rrrrr r   r r   r   r   r   r r   r r   r",
]

for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x, y, pen)
    
wn.mainloop()
