n= int(input())
a=[]
b=[]
for i in range(n):
    x,y = input().split()
    a.append(x)   
    b.append(y)
m=0
k=0
str=""
for i in range(n):
    if b.count(b[i])>m:
        m=b.count(b[i])
        k=i;
for i in range(n):
    if b[i]==b[k]:
        str= str + a[i] +" "
print(str)
        
