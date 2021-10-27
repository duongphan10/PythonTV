s = str(input())
s1= "TRẺTRÂU"
k=0
for i in range(len(s)): 
    # print(s[i])
    if (s[i]==s1[k]):
        k+=1
if k==len(s1):
    print("TRẺ TRÂU")
else:
    print("Không TRẺ TRÂU")
