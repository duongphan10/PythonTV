a,b = input().split()
k = len(a)
h = len(b)
ans = 0 
for i in range(0,h-k+1):
    if (a== b[i:i+k] ):
        ans+=1
print(ans)