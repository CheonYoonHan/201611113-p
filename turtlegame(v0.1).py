#거북이 키우기(ver 0.1)
#간단한 설명: 1분내에 아이템을 먹으며 거북이를 키우면 된다.

#거북이 만든다.
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

#배경설정
wn.bgpic("turtle.gif")

#거북이 기본설정
t1.shape("turtle")
ts=1
t1.shapesize(ts,ts,ts)
t1.pencolor("green")
t1.speed(5)
t1.penup()
track=list()

#거북이 키보드로 반응하게 하기

#스코어 계산하기

#게임 시간 설정하기

#별 아이템을 먹었을때(점수+1)
if t1.pos()==(1,1) or (-100,100) or (350,-50) or (-45,-100):
    track.append(t1.pos())
    ts=ts+0.2
    t1.shapesize(ts,ts,ts)
    print Score +1

#파란원 아이템을 먹었을 때(점수+1)
if t1.pos()==(125,35):
    track.append(t1.pos())
    t1.pencolor('blue')

#사각형 아이템을 먹었을 때
if t1.pos()==(50,-50):
	ts=ts-0.2
	t1.shapesize(ts,ts,ts)

#나선 모양 아이템을 먹었을 때
if t1.pos()==(-200,200):
    track.append(t1.pos())
    def makeswirlsquare(size,bigger,sides,angle):
    	for i in range(0,sides): 
        	if i % 2==0:
            		size=size+bigger
        	t1.fd(size)
        	t1.right(angle)

    makeswirlsquare(1,2,10,90)

#초록원 아이템을 먹었을 떄
if t1.pos==(-200,50):
    track.append(t1.pos())
    t1.speed(3)

#삘긴원 아이템을 먹었을 때
if t1.pos==(100,200):
    track.append(t1.pos)
    t1.speed(7)