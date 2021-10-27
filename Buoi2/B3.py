s = str(input("Nhập chuỗi dài hơn 10: "))
while len(s)<=10:
    s = str(input("Nhập lại chuỗi dài hơn 10: "))
print("Độ dài chuỗi: ",len(s))
print("Slicing 2->6: ",s[1:5])

s = str(input("Nhập chuỗi: "))
print("Chuỗi viết hoa: ",s.upper())
print("Chuỗi viết thường: ",s.lower())
print("Chuỗi sau khi thay thế: ",s.replace("b","g"))
s=str("hElLo-mY-NAMe-iS-SuZIe")
s= s.lower()
s= s.replace("-"," ")
s1=""
for i in range(len(s)):
    if i==0 or (i>=1 and s[i-1]==" "):
        s1+=s[i].upper()
    else:
        s1+=s[i]
print(s1)