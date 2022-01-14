aList = list(map(int,input().split()))
aList = sorted(aList)
b,c = [],[]
i=0
while i<len(aList):
    b.append(aList[i])
    while i+1<len(aList) and aList[i+1]==aList[i]:
        b.append(aList[i+1])
        i+=1
    c.append(b)
    b= []
    i+=1
print(c)