#데이터구조-2: 거북이 트랙을 저장하기
def drawSquareAt(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.setheading(90)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.right(90)
        t1.fd(size)
    return tracks
def savepos():
    #리스트로 4개 점 지정하기
    list1=list()
    list1.append((100,0))
    list1.append((100,100))
    list1.append((0,100))
    list1.append((0,0))
    #튜플로 4개 점 지정하기
    tuple1=((150,0),(150,150),(0,150),(0,0))   

def drawSquareFrom(tracks):
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        t1.goto(tracks[i])
def lab7a():
    mytracka=drawSquareAt(100,(0,0))
    print mytracka
def lab7b():
    savepos()
    mytrackb=drawSquareFrom(tuple1)
def main1():
    lab7a()
def main2():
    lab7b()
