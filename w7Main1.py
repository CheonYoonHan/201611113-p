#리스트 함수 정의
x=list()
def l():
	for i in range(0,1000):
		if i % 4==0 and i%5!=0:
			x.append(i)
def main1():
	l()
	print x
#리스트 합 구하는 함수 정의
def sumlist(alist):
	mysum=0
	for i in range(0,len(alist)):
		mysum=mysum+x[i]
	return mysum
def lab6():
	l()
	alist=x
	labsum=sumlist(alist)
	print labsum
def main2():
	lab6()
#리스트 보이기
main1()
#리스트 합 구하기
x=list()
main2()
input()