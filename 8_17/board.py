import turtle,random
turtle.speed(0)
turtle.tracer(1200)
turtle.hideturtle()
turtle.colormode(255)
turtle.bgcolor(220,200,170)
turtle.penup()
turtle.seth(270)
for i in range(8000):
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    p=random.randint(0,50)
    turtle.goto(x,y)
    turtle.pencolor(255-144*p//100,255-184*p//100,255-208*p//100)
    turtle.pendown()
    turtle.forward(random.randint(20,100))
    turtle.penup()
turtle.pencolor(0,0,0)
turtle.seth(0)
turtle.goto(-280,280)
for i in range(16):
    turtle.pendown()
    if i%15==0:
        turtle.pensize(4)
    else:
        turtle.pensize(2)
    turtle.forward(560)
    turtle.penup()
    turtle.goto(-280,280-i*40)
turtle.seth(270)
turtle.goto(-280,280)
for i in range(16):
    turtle.pendown()
    if i%15==0:
        turtle.pensize(4)
    else:
        turtle.pensize(2)
    turtle.forward(560)
    turtle.penup()
    turtle.goto(-280+i*40,280)
point=[(0,0),(160,160),(-160,160),(160,-160),(-160,-160)]
for i in point:
    turtle.goto(i)
    turtle.dot(8)
turtle.done()