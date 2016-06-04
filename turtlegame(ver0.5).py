#거북이 만든다.
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
#거북이 만든다.
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

#배경을 그리자.
bg=open('background.txt')
mycoords=[]
t1.pensize(3)
t1.speed(10)
for i in range(0,28,2):
    for line in fres:
        line1=line.split(',')
        mycoords.append(line[i],line1[i+1].strip())
for coord in mycoords:
    x1=int(coord[0])
    y1=int(coord[1])
    x2=int(coord[2])
    y2=int(coord[3])
    x3=int(coord[4])
    y3=int(coord[5])
    x4=int(coord[6])
    y4=int(coord[7])
    x5=int(coord[8])
    y5=int(coord[9])
    x6=int(coord[10])
    y6=int(coord[11])
    x7=int(coord[12])
    y7=int(coord[13])
    x8=int(coord[14])
    y8=int(coord[15])
    x9=int(coord[16])
    y9=int(coord[17])
    x10=int(coord[18])
    y10=int(coord[19])
    x11=int(coord[20])
    y11=int(coord[21])
    x12=int(coord[22])
    x12=int(coord[23])
    x13=int(coord[24])
    x13=int(coord[25])
    x14=int(coord[26])
    y14=int(coord[27])
def back(pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.circle(10)
t1.pencolor('black')
back(x1,y1)
back(x2,y2)
back(x3,y3)
back(x4,y4)
back(x5,y5)
t1.pencolor('yellow')
back(x6,y6)
back(x7,y7)
t1.pencolor('red')
back(x8,y8)
back(x9,y9)
back(x10,y10)
back(x11,y11)
back(x12,y12)

#거북이 프로필
t1.shape("turtle")
ts=1
t1.shapesize(ts,ts,ts)
t1.pencolor("green")
sp=5
t1.speed(sp)
t1.penup()
pos=t1.pos

#거북이를 움직이게 하자.
def keyup():
    t1.forward(50)
    circle((300,1),10,pos)
    circle((-50,-300),10,pos)
    circle((100,100),10,pos)
    circle((-150,50),10,pos)
    circle((430,-300),10,pos)
    ycircle((280,11),10,pos)
    ycircle((-170,10),10,pos)
    bcircle((-400,300),10,pos)
    bcircle((100,250),10,pos)
    rcircle((-150,-170),10,pos)
    rcircle((400,30),10,pos)
    rcircle((-170,50),10,pos)
    gcircle((30,-150),10,pos)
    gcircle((-100,350),10,pos)
def keydown():
    t1.back(50)
    circle((300,1),10,pos)
    circle((-50,-300),10,pos)
    circle((100,100),10,pos)
    circle((-150,50),10,pos)
    circle((430,-300),10,pos)
    ycircle((280,11),10,pos)
    ycircle((-170,10),10,pos)
    bcircle((-400,300),10,pos)
    bcircle((100,250),10,pos)
    rcircle((-150,-170),10,pos)
    rcircle((400,30),10,pos)
    rcircle((-170,50),10,pos)
    gcircle((30,-150),10,pos)
    gcircle((-100,350),10,pos)
def keyright():
    t1.right(10)
def keyleft():
    t1.left(10)
def keybord():
    wn.onkey(keyup, "Up")
    wn.onkey(keyright, "Right")
    wn.onkey(keyleft, "Left")
    wn.onkey(keydown, "Down")

#거북이 먹이
import math
def circle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        ts=ts+0.2
        t1.shapesize(ts,ts,ts)
        print Score +1
def ycircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        ts=ts-0.2
        t1.shapesize(ts,ts,ts)
        print Score -1
def bcircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        t1.pencolor('blue')
        print Score +1
def rcircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        sp=sp+1
        t1.pencolor('red')
        t1.speed(sp)
        print Score +1
def gcircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        sp=sp-1
        t1.pencolor('green')
        t1.speed(sp)
        print Score -1

#게임을 시작하자.
def game():    
    keybord()
    wn.listen()
    turtle.mainloop()
game()