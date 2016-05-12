import math

def NearLocation(ky,locations):
    dist=[]
    for (x,y) in locations:
        dist.append(math.sqrt((ky[0]-x)**2 + (ky[1]-y)**2))
    return min(dist)
def main1():
    ky=(37.5758422,126.9713913)
    locations=[(37.5730979,126.9739731)
    ,(37.5701732,126.9809103)
    ,(37.5765602,126.9832833)
    ,(37.5704272,126.9899833)
    ,(37.5657079,126.9746729)]
    NearLocation(ky,locations)

seoul=[[74425,76326],
[61164, 61,636],
[109688, 115744],
[144796, 146776],
[174996, 181676],
[177841, 177434],
[204630, 205980],
[223373, 232245],
[161055, 166130],
[171576, 176735],
[279169, 293772],
[239450, 251066],
[148690, 156510],
[182977, 196992],
[237792, 242641],
[283869, 296762],
[209344, 210282],
[118965, 114441],
[186503, 186856],
[195734, 203014],
[254381, 249472],
[212401, 229111],
[271654, 295354],
[319197, 335045],
[229829, 231671],]
import matplotlib
import matplotlib.pyplot as plt
def summan():
    man=0
    for i in range(0,len(seoul)):
        man=man+seoul[i][0]
    print '서울에 사는 남자의 총수는 {0:d}입니다' .format(man)
def sumwoman():
    woman=0
    for i in range(0,len(seoul)):
        woman=woman+seoul[i][0]
    print '서울에 사는 여자의 총수는 {0:d}입니다' .format(woman)
def averageman():
    sum=0
    for i in range(0,len(seoul)):
        sum=sum+(seoul[i])
    print sum/len(seoul)
def averagewoman():
    sum=0
    for i in range(0,len(seoul)):
        sum=sum+(seoul[i])
    c=sum/len(seoul)
def sumGu():
    sumgu=list()
    for gu in seoul:
        sumgu.append(gu[0]+gu[1])
    plt.bar(range(len(sumgu)), sumgu, align='center')
    plt.show()
def main2():
    summan()
    sumwoman()
    averageman()
    averagewoman()
    sumGu()
