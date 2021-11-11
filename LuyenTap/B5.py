s = str(input())
k = len(s)
ans=0
for i in range(k):
    for j in range(i+1,k):
        val=0
        x = i
        y = j
        while s[i]==s[j] and y<k:
            val+=1
            x+=1
            y+=1
        ans= max(ans,val)
print(ans)