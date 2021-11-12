n = input()
a = list(map(int,input().split()))
a.sort()
b = []
ans = 0
for i in a:
    sum =0
    for j in range(1,i):
        if (i%j==0):
            sum+=j
    if (sum>i):
        ans+=1
        b.append(i)
print(ans)
print(*b)
    