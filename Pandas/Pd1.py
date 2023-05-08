import pandas as pd

s = pd.Series(data = [1,2,3,4],index= ['one','two','three','fo'])
s1 = pd.Series(data= [6,5,4,3,2],index= ['one','two','three','fo','fi'])

d = pd.concat([s,s1], axis= 1,)
print(d)
print(d[0:2])