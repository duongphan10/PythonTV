a = int(input("Nhap a: "))
while a>9:
    b=a
    a=0
    while (b>0):
        a+=b%10
        b//=10
    # print(a)
print(a)
    