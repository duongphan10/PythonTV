s = str(input())
k = len(s)
if k<2:
    print("")
else:
    print(s[0:2]+s[k-2:k])