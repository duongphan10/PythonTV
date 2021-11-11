a = []
b = []
c = []
def Input():
    n = int(input())
    a = list(map(int,input().split()))
    return a
def Check():
    a.sort()
    i =0
    while (i<len(a)):
        k=1        
        while (i+1<len(a) and a[i]==a[i+1]):
            i+=1
            k+=1
        b.append(a[i])
        c.append(k)
        i+=1
def Output():
    for i in range(len(b)):
        print(b[i],':',c[i])
a =Input()
Check()
Output()

