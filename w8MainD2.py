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
    print tracks
def lab8():
    drawSquareAt(100,(0,0))
def main():
    lab7()
