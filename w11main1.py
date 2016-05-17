import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye:
        t1.color('red')
        sqaure(50)
def sqaure(size):
    t1.penup()
    t1.goto(100,100)
    t1.setheading(0)
    t1.pendown()
    for i in range(0,4):
        t1.fd(size)
        t1.left(90)
    t1.penup()
    t1.home()

def game():
    sqaure(100)
    keybord()
    mouse()
    wn.listen()
    turtle.mainloop()
def main1():
    game()
#5
def line():
    t1.penup()
    t1.goto(0,-100)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.home()
def isOnLine(point, pos1, pos2):
    if x1<=point[0]<=x2 and y1<=point[1]<=y2:
        t1.color('red')
        line()
def game2():
    line()
    line1=[(50,100),(150,100)]
    x1=line1[0][0]-1
    y1=line1[0][1]-1
    x2=line1[1][0]+1
    y2=line1[1][1]+1
    pos1=(x1,y1)
    pos2=(x2,y2)
    keybord()
    mouse()
    wn.listen()
    turtle.mainloop()
def main2():
    game2()
    
#6
import math
def isInCircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        t1.color('green')
        t1.circle(50)
def Circle():
    t1.penup()
    t1.goto(100,0)
    t1.pendown()
    t1.circle(100)
    t1.penup()
    t1.home()
    

def game3():
    Circle()
    keybord()
    mouse()
    wn.listen()
    turtle.mainloop()

def main3():
    game3()
    
#option
def keyup():
    t1.forward(50)
    curpos=t1.pos()
    coord = [(100,100),(200,200)]
    isInRectangle(curpos,coord)
    isOnLine(point,pos1,pos2)
    isInCircle((100,100),100,pos)
def keydown():
    t1.back(50)
def keyright():
    t1.right(10)
def keyleft():
    t1.left(10)
def mousegoto(x,y):
    t1.setpos(x,y)
    curpos=t1.pos()
    coord = [(100,100),(200,200)]
    isInRectangle(curpos,coord)
    isOnLine(point,pos1,pos2)
    isInCircle((100,100),100,pos)
def keybord():
    wn.onkey(keyup, "Up")
    wn.onkey(keyright, "Right")
    wn.onkey(keyleft, "Left")
    wn.onkey(keydown, "Down")
def mouse():
    wn.onclick(mousegoto)
