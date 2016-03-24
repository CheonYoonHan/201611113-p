#섭씨를 화씨로, 화씨를 섭씨로 변환하기
temp=input("User input temprtature : ")
sel=raw_input("Fahrenheit or Celsius(F or C) : ")
print "%.1f" %temp, sel
if sel=="F":
    result=(temp-32)/1.8
    print "%.1f" %result,"C"
elif sel=="f":
    result=(temp-32)/1.8
    print "%.1f" %result,"C"
elif sel=="C":
    result=temp*1.8+32
    print "%.1f" %result,"F"
elif sel=="c":
    result=temp*1.8+32
    print "%.1f" %result,"F"
else:
    print "input Error"

me=raw_input("Correctly? (Yes or No) : ")
if me=="Yes":
    print "Thank you"
elif me=="yes":
    print "Thank you"
elif me=="No":
    print "Sorry"
elif me=="no":
    print "Sorry"


