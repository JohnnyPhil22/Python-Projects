import turtle

WIDTH = 985
HEIGHT = 170

wn = turtle.Screen()
wn.title("Lite-Brite Simulator by Jonathan")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)

color_codes = {
    "r":"red",
    "g":"green",
    "b":"blue",
    "w":"white",
    " ":"black"
}

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
"                            wwwwwww             ",
"rrr rrr rrr rr  rrr   g  g  w     w  bbb b b bbb",
"r   r r r r r r r    gg gg  w www w   b  b b b  ",
"r   rrr rrr r r rrr   g  g  w w w w   b  bbb bbb",
"r r rr  r r r r r     g  g  w wwwww   b  b b   b",
"rrr r r r r rr  rrr   g  g  w        bbb b b bbb",
"                            wwwwwww             ",
]

# Draw picture
for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x, y, pen)
    
wn.mainloop()
