a = list(input().split("+"))
a.sort()
s = str(a[0])
for i in range(1,len(a)):
    s = s + '+' + str(a[i])
print(s)