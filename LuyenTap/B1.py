s = str(input())
x = s[s.index('(')+1:len(s)-1]
x = list(x.split(','))
print(*x)