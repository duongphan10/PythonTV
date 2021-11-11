a = str(input())
while (len(a)>1):
    a = str(sum( int(a[i]) for i in range(len(a))))
print(a)

    