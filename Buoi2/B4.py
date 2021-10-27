aList = list(map(int, input("Nhap mang: ").split())) 
k = int(input("Nhap k: "))
result=0
for i in range(len(aList)):
    for j in range(i+1,len(aList)):
        if aList[i]+aList[j]==k:
            result+=1
print("result = ",result)