a = list(map(int,input().split()))
x = int(input())
def Check():
    if x in a:
        print(a.index(x))
        a.remove(x)
def Del():
    while (x in a):
        a.remove(x)
Check()
Del()
y = int(input())
def Swap():
    if (y<len(a)):
        a[y]=x
Swap()
