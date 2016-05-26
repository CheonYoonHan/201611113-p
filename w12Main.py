%cd 'C:\Users\P400\Documents\p162
import time
def modify():
    msg='[cyh edited [0]]' .format(time.strftime('%d-%m-%Y %H:%M:%S' ))
    file1=open('output.txt','w')
    line1='first line\n'
    file1.write(line1)
    line2='second line\n'
    file1.write(line2)
    line3='third\n'
    file1.write(line3)
    filetwo.close()
    fin=open('output.txt','r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        for word in words:
            if word=='line':
                fout.write('/t')
                word=word.upper()
            fout.write(word)
        fout.write('/n')
    fin.close()
    fout.close()
def data1():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        str="{0}\t" .format(i)
        fout.write(str)
        if i%2==0:
            fourt.write('\n')
    fout.close()

def lab12():
    modify()
    data1()

def main():
    lab12()
    %load outputNumber.txt
