#문자로 삼각형 그리기(제어-7)
def tri(number):
    for i in range(1,number+1):
        print " "*(number-i)+"#"*(i*2-1)
tri(10)