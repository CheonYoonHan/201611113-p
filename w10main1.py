allData=[
    ["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes","No"],
    ["Affogato","No","No","Yes"]
]
def coffee():
    data1=allData[1:]
    data2=list()
    for i,d in enumerate(allData):
        if i>0:
            data2.append(d)
    count=0
    for i in data1:
        if i[2].upper()=='YES':
            count+=1
    print "Number of Coffee adding Milk",count
    print "% of coffee with milk: ",100*count/float(len(data1))
def main1():
    coffee()
marks=[
    ['Subject','scores'],
    ['English', 100],
    ['Math', 80],
    ['English', 70],
    ['Math', 100],
    ['English', 82.3],
    ['Math', 98.5]
]

def jum():
    marks=marks[1:]
    englishSum=0
    mathSum=0
    englishCount=0
    mathCount=0
    for row in marks:
        subj = row[0]
        mark = int(row[1])
        if subj=="English":
            englishSum+=mark
            englishCount+=1
        elif subj=="Math":
            mathSum+=mark
            mathCount+=1
        else:
            pass
    print mathSum,englishSum
    print float(mathSum/mathCount),float(englishSum/englishCount)
def main2():
    jum()

letitbe=[
    ["When I find myself in times of trouble"],
    ["Mother Mary comes to me"],
    ["Speaking words of wisdom, let it be"],
    ["And in my hour of darkness"],
    ["She is standing right in front of me"],
    ["Speaking words of wisdom, let it be"],
    ["Let it be"],
    ["Let it be"],
    ["Let it be"],
    ["Let it be"],
    ["Whisper words of wisdom, let it be"]
]

def countWords(letit):
    d = {}
    for sentence in doc:
        words=sentence.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
    return d

def getWordsFreqGreater(c,d):
    w=list()
    for k in d:
        if d[k]>c:
            w.append(k)
def main3():
    return w
    wordDict=countWords(doc)
    freqWordsList=getWordsFreqGreater(2,wordDict)
    print "Frequent words: ",freqWordsList



