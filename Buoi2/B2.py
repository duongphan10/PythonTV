aList = list(map(int, input().split())) 
for i in range(1,len(aList)):
    aList[i]+=aList[i-1]
print(aList)
