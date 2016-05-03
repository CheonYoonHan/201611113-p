import matplotlib
import matplotlib.pyplot as plt
def charCount(word):
    a=dict()
    for i in word:
        if i not in a:
            a[i]=1
        else:
            a[i]=a[i]+1
    return a
def main():
	word='sangmyung university'
	print charCount(word)
def Drawgraph:
	c=charCount(word)
	plt.bar(range(len(c)), c.values())
	plt.xticks(range(len(c)), list(c.keys()))
	plt.show()
def charCount2(word):
	b=dict({"digit" : 0, "alpha" : 0})
	for i in word :
    	if i.isdigit() :
        	b["digit"]+=1
    	elif i.isalpha() :
        	b["alpha"]+=1
    	return d
def main2():
	word="sangmyung university 20, hongjimun 2-gil, jongno-gu, seoul 03016, republic of korea "
	print charCount2(word)
def Drawgraph2:
	d=charCount2(word)
	plt.bar(range(len(d)), d.values())
	plt.xticks(range(len(d)), list(d.keys()))
	plt.show()
def house:
	mh=set(['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
	fh=({'offee machine', 'adio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'})
	return mh&fh
def main3():
	print house()