Data1=[ 
    [13.1, 37.1], 
    [10.6, 34.6], 
    [27.1, 40.0], 
    [16.2, 37.8], 
    [11.4, 29.8], 
    [12.2, 26.5], 
    [13.5, 29.7], 
    [13.7, 37.6]] 
Data2=[ 
    [8.7, 1.5], 
    [13.4, 1.9], 
    [2.9, 1.5], 
    [6.8, 0.8], 
    [14.8, 4.9], 
    [14.9, 4.4], 
    [11.1, 2.4], 
    [4.1, 1.2]] 
def survey():
    sum1=0  
    for i in Data1: 
        sum1=i[0]+i[1]  

    sum2=0 
    for x in Data2: 
        sum2=x[0]+x[1] 
 
    print "만족도의 합 :",sum1 
    print "불만족도의 합 :",sum2
    print "만족도의 평균:",float(sum1/len(Data1)) 
    print "불만족도의 평균 :",float(sum2/len(Data2)) 

def main():
    survey()
