aList = list(map(str,input().split()))
s= set()
def xd10(x):
    bList=[]
    for i in range(len(x)):
        if x[i]=='1' or x[i]=='0':
            bList.append(i)
    return tuple(bList)
def ss10(x):
    s.add(x)
for i in aList:
    ss10(xd10(i))
print(len(s))
