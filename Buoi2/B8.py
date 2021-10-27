a= input()
s= a.count("1")
if s%2==1:
    print("NO")
else:
    k=0
    for i in range(len(a)):
        if (a[i]=="1"):
            k+=1
        if k==s/2:
            print(a[:i+1]," ",a[i+1:])
            break
