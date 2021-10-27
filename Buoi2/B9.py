s = input()
aList=[]
bList=[]
for i in range(len(s)):
    if s[i]!="‘" and s[i]!="’" and s[i]!=",":
        if int(s[i])%2==0:
            aList.append(int(s[i]))
        else:
            bList.append(int(s[i]))
print(tuple(aList + bList))
