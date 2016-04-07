#윤년 계산하기
print "calculate Leap Year"
year=input("User input year : ")
if year==(year%4 == 0) and (year%100 !=0 or year%400==0):
    print "User inputing year is Leap Year"
else:
    print "User inputing Year is Leap Year"
