a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    if a[i]%2==1:
        b.append(i)
print(*b)
k = 0
for i in range(len(b)):
    del a[b[i]-k]
    k+=1
print(a)