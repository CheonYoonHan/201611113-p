#high & low game
print "Think your number (1~10)!"
print ("Game Start!")
f=raw_input("Your number is higher than 5?(Y or N) : ")
if f=="Y":
    s=raw_input("Your number is lower than 7?(Y or N) : ")
    if s=="Y":
        "Your number is 6!!!"
    elif s=="N":
        se=raw_input("Your number is 7?(Y or N) : ")
        if se=="Y":
            print "Your number is 7!!"
        elif se=="N":
            n=raw_input("Your number is lower than 9(Y or N) : ")
            if n=="Y":
                print "Your number is 8!!!"
            elif n=="N":
                ni=raw_input("Your number is 9?(Y or N) : ")
                if ni=="Y":
                    print "Your number is 9!!!"
                elif ni=="N":
                    print "Your number is 10!!!"
elif f=="N":
    fi=raw_input("Your number is 5?(Y or N) : ")
    if fi=="Y":
        print "Your number is 5!!!"
    elif fi=="N":
        t=raw_input("Your number is higher than 3?(Y or N) : ")
        if t=="Y":
            print "Your number is 4!!!"
        elif t=="N":
            th=raw_input("Your number is 3?(Y or N) : ")
            if th=="Y":
                print "Your number is 3!!!"
            elif th=="N":
                o=raw_input("Your number is higher than 1?(Y or N) : ")
                if o=="Y":
                    print "Your number is 2!!!"
                elif o=="N":
                    print "Your number is 1!!!"
