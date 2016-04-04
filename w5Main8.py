def BMI():
    height=input ("input user height (cm): ")
    weight=input ("input user weight (kg): ")
    print "%.1f" %height, "%.1f" %weight
    BMI=weight*10000/(height*height)
    print "%.1f" %BMI
    if BMI<=18.5:
        res= 'Low weight'
    elif 18.5<BMI<23:
        res= 'Nomal weight'
    elif 23<=BMI<25:
        res= 'Over weight'
    else:
        res= 'Very Over weight'
    return res
print BMI()