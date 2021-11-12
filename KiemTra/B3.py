import math
n = input()
a = list(map(int,input().split()))
ans =0
for i in a:
    sum = 0
    k= int(math.sqrt(i))
    for j in range(2,k+1):
        if i%j==0:
            sum+=2
    if k*k == i:
        sum-=1
    if sum==1:
        ans+=1
print(ans)
