def check(A,B):
    print(A-B)
    if (A-B==set()):
        print("La tap con")
    else:
        print("Ko la tap con")
aList = set(map(str,input().split()))
bList = set(map(str,input().split()))
check(aList,bList)

