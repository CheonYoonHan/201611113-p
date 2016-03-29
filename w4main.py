# coding: utf-8
#바람개비 모형 그리기 다이어그램
%%plantuml
@startuml
start
:set size, bigger, sides, angle;
repeat
if (i is multiples of 2) then
    :size=existing size+bigger;
endif
:t1.fd(size);
:t1.right(angle);
repeat while(sides)
stop
@enduml

#거북이
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

#바람개비 모형 그리는 함수 정의
def makeswirlsquare(size,bigger,sides,angle):
    for i in range(0,sides): 
        if i % 2==0:
            size=size+bigger
        t1.fd(size)
        t1.right(angle)

#바람개비 모형 그리기
makeswirlsquare(10,10,50,90)

