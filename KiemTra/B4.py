s = str(input())
def Check(a):
    k = len(a)
    i =0
    ans= 0
    s1 =""
    while (i<k):
        ans=1
        j=i+1
        while(j<k and a[j]==a[i]):
            j+=1
            ans+=1
        s1= s1+ str(ans) + str(a[i])
        i=j
    #print(s1)
    return s1
s = Check(s)
print(s)
print(Check(s))


        