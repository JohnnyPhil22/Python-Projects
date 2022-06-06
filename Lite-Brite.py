import turtle

WIDTH = 985
HEIGHT = 170

wn = turtle.Screen()
wn.title("Lite-Brite Simulator by Jonathan")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)

color_codes = {"v":"violet","i":"indigo","b":"blue","g":"green","y":"yellow","o":"orange","r":"red","w":"white"," ":"black"}

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
"vvvvv iiiii bbbbb ggggg       yyyyy ooooo rrrrr",
"  v   i   i     b     g       y   y o   o     r",
"  v   i   i     b     g       y   y o   o     r",
"  v   iiiii bbbbb ggggg       y   y o   o    r ",
"v v   i     b     g           y   y o   o   r  ",
"v v   i     b     g           y   y o   o  r  ",
"vvv   i     bbbbb ggggg wwwww yyyyy ooooo r   ",
]

# Draw picture
for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x, y, pen)
    
wn.mainloop()
