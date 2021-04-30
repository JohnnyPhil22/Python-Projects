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
    "o":"orange",
    "y":"yellow",
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
"rrr ggg bbb ooo yyy   r  g  w     w  bbb o o yyy",
"r   g g b b o o y    rr gg  w www w   b  o o y"  ,
"r   ggg bbb o o yyy   r  g  w w w w   b  ooo yyy",
"r r gg  b b o o y     r  g  w wwwww   b  o o   y",
"rrr g g b b ooo yyy   r  g  w        bbb o o yyy",
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
