import turtle

lw = rw = 6
ly = ry = 80

gscreen = turtle.Screen()
gscreen.title("Glow Hockey")
gscreen.bgcolor("White")
gscreen.setup(width=1000, height=600)

l_pad = turtle.Turtle()
l_pad.speed(0)
l_pad.shape("square")
l_pad.color("#00C78C")
l_pad.shapesize(stretch_wid=lw, stretch_len=2)
l_pad.penup()
l_pad.goto(-400, 0)

r_pad = turtle.Turtle()
r_pad.speed(0)
r_pad.shape("square")
r_pad.color("#00C78C")
r_pad.shapesize(stretch_wid=rw, stretch_len=2)
r_pad.penup()
r_pad.goto(400, 0)

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("brown3")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

player1 = 0
player2 = 0

display = turtle.Turtle()
display.speed(0)
display.color("blue")
display.penup()
display.hideturtle()
display.goto(0, 240)
display.write("PLAYER 1 : 0      PLAYER 2 : 0", align="center", font=("Times New Roman", 24, "bold"))

def p1padup():
    y = l_pad.ycor()
    y += 20
    if y < 250:
        l_pad.sety(y)

def p1paddown():
    y = l_pad.ycor()
    y -= 20
    if y > -250:
        l_pad.sety(y)

def p2padup():
    y = r_pad.ycor()
    y += 20
    if y < 250:
        r_pad.sety(y)

def p2paddown():
    y = r_pad.ycor()
    y -= 20
    if y > -250:
        r_pad.sety(y)

gscreen.listen()
gscreen.onkeypress(p1padup, "w")
gscreen.onkeypress(p1paddown, "s")
gscreen.onkeypress(p2padup, "Up")
gscreen.onkeypress(p2paddown, "Down")

while True:
    if rw > 15:
        display.goto(0, 20)
        display.color("red")
        display.write("PLAYER 1 WON!", align="center", font=("Times New Roman", 30, "bold"))
        gscreen.update()
        continue

    if lw > 15:
        display.goto(0, 20)
        display.color("red")
        display.write("PLAYER 2 WON!", align="center", font=("Times New Roman", 30, "bold"))
        gscreen.update()
        continue

    gscreen.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 300:
        ball.sety(280)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    
    if ball.xcor() > 500:
        ball.goto(0,0)
        ball.dy *= -1
        player1 += 1
        display.clear()
        display.write("PLAYER 1 : {}      PLAYER 2 : {}".format(player1, player2), align= "center", font = ("Times New Roman", 24, "bold"))
        rw+=1
        ry+=10
        r_pad.shapesize(stretch_wid=rw, stretch_len=2)

    if ball.xcor() < -500:
        ball.goto(0,0)
        ball.dy *= -1
        player2 += 1
        display.clear()
        display.write("PLAYER 1 : {}      PLAYER 2 : {}".format(player1, player2), align= "center", font = ("Times New Roman", 24, "bold"))
        lw+=1
        ly+=10
        l_pad.shapesize(stretch_wid=lw, stretch_len=2)

    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < r_pad.ycor()+ry and ball.ycor() > r_pad.ycor()-ry):
        ball.setx(360)
        ball.dx *= -1
        if rw>6:
            rw -= 1
            ry -= 10
        else:
            rw=6
            ry=80
        r_pad.shapesize(stretch_wid=rw, stretch_len=2)

    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < l_pad.ycor()+ly and ball.ycor() > l_pad.ycor()-ly):
        ball.setx(-360)
        ball.dx *= -1
        if lw>6:
            lw -= 1
            ly -= 10
        else:
            lw=6
            ly=80
        l_pad.shapesize(stretch_wid=lw, stretch_len=2)