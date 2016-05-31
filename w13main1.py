import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def plus():
    file1="python.txt"
    file2="Number.txt"
    try:
        fin1=open(file1, 'a')
        fin2=open(file2, 'r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
        
def save():
    %%writefile reccoords.txt
    0,0,100,100
    200,200,150,150

def record():
    frec=open('reccoords.txt','r')
    mycoords=[]
    for line in frec:
        line1=line.split(',')
        #print [(line1[0], line1[1]), (line1[2], line1[3].strip())]
        mycoords.append([(line1[0], line1[1]), (line1[2], line1[3].strip())])
    frec.close()

def draw(coords):
    for coord in coords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[1][1])
        y2=int(coord[0][1])
    t1.penup()
    t1.goto(x1,y1)
    t1.pendown()
    t1.goto(x2,y1)
    t1.goto(x2,y2)
    t1.goto(x1,y2)
    t1.goto(x1,y1)
def lab1():
    plus()

def lab2():
    save()
    record()
    draw(mycoords)

def main():
    lab1()
    lab2()
