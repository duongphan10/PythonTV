aList = list(map(int, input().split())) 
k = int(input())
result=sum( aList[i+1:].count(k-aList[i]) for i in range(len(aList)))

print(result)