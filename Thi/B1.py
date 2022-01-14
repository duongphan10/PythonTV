a,b,n = map(int,input().split())
list =[]
for i in range(a,b+1):
    if i%n==0:
        list.append([i,i*i])
print(dict(list))
