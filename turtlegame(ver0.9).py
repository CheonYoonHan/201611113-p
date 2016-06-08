#거북이 만든다.
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

#배경을 그리자
bg=open('background.txt', 'r')
mycoords=[]
for i in range(1,29):
    for line in bg:
        line1=line.split(',')
    mycoords.append((line1[i]))
bg.close()
x1=int(mycoords[0])
y1=int(mycoords[1])
x2=int(mycoords[2])
y2=int(mycoords[3])
x3=int(mycoords[4])
y3=int(mycoords[5])
x4=int(mycoords[6])
y4=int(mycoords[7])
x5=int(mycoords[8])
y5=int(mycoords[9])
x6=int(mycoords[10])
y6=int(mycoords[11])
x7=int(mycoords[12])
y7=int(mycoords[13])
x8=int(mycoords[14])
y8=int(mycoords[15])
x9=int(mycoords[16])
y9=int(mycoords[17])
x10=int(mycoords[18])
y10=int(mycoords[19])
x11=int(mycoords[20])
y11=int(mycoords[21])
x12=int(mycoords[22])
y12=int(mycoords[23])
x13=int(mycoords[24])
y13=int(mycoords[25])
x14=int(mycoords[26])
y14=int(mycoords[27])
    
def back(pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.circle(10)
t1.pensize(3)
t1.speed(10)
t1.pencolor('black')
back((x1,y1))
back((x2,y2))
back((x3,y3))
back((x4,y4))
back((x5,y5))
t1.pencolor('yellow')
back((x6,y6))
back((x7,y7))
t1.pencolor('blue')
back((x8,y8))
back((x9,y9))
t1.pencolor('red')
back((x10,y10))
back((x11,y11))
back((x12,y12))
t1.pencolor('green')
back((x13,y13))
back((x14,y14))

#먹이를 설정하자.
import math
def circle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        global ts
        ts=ts+0.5
        t1.shapesize(ts,ts,ts)
        global Score
        Score=Score+5
        print 'Score +5'
def ycircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        t1.pencolor('yellow')
        global ts
        ts=ts-0.5
        t1.shapesize(ts,ts,ts)
        global Score
        Score=Score-10
        print 'Score -10'
def bcircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        t1.pencolor('blue')
        Score=Score+1
        global Score
        Score=Score+1
        print 'Score +1'
def rcircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        t1.pencolor('red')
        global sp
        sp=sp+2
        t1.speed(sp)
        global Score
        Score=Score+3
        print 'Score +3'
def gcircle(center, radius, pos):
    if 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius:
        t1.pencolor('green')
        global sp
        sp=sp-2
        t1.speed(sp)
        global Score
        Score=Score-5
        print 'Score -5'

#거북이 설정하자.
t1.shape("turtle")
ts=1
t1.shapesize(ts,ts,ts)
t1.pencolor("green")
sp=5
t1.speed(sp)
t1.penup()
Score=0
t1.home()

#거북이 키보드로 반응하게 하기
def keyup():
    t1.forward(30)
    pos=t1.pos()
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
    t1.back(20)
    pos=t1.pos()
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

#게임을 시작하자.
def game():
    print "Game start"
    keybord()
    wn.listen()
    turtle.mainloop()
p=open('score.txt','a')
if ts>=5:
    print 'game end!'
    print Score
    name=raw_input("input your name: ")
    msg='p {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
    print "player"+'\n' +Score+ '\t'+ str(number) +'\t' + msg
    p.write('\n' + Score + '\t'+ str(number) +'\t' + msg)
    p.close()
    wn.exitonclick()
game()
