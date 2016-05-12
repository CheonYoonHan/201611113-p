import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def sqaure():
    t1.penup()
    t1.goto(-100,0)
    t1.setheading(90)
    t1.pendown()
    t1.fd(25)
for i in range(0,4):
    t1.right(90)
    t1.fd(50)
t1.penup
t1.home
def keyup():
    t1.forward(50)
def keydown():
    t1.back(50)
def keyright():
    t1.right(10)
def keyleft():
    t1.left(10)
def mousegoto(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y)
    if -125<x<75 and -25<y<25:
        print 'success!'
def keybord():
    wn.onkey(keyup, "Up")
    wn.onkey(keyright, "Right")
    wn.onkey(keyleft, "Left")
    wn.onkey(keydown, "Down")
def mouse():
    wn.onclick(mousegoto)
sqaure()
keybord()
mouse()
wn.listen()
turtle.mainloop()
