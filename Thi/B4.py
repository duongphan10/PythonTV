import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv("Data.csv")
print(df)
df1 = df.copy()
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(df1.iloc[:,1:3])
df1.iloc[:,1:3] = imputer.transform(df1.iloc[:,1:3])
print(df1)
a = df1["Country"]
b = df1["Salary"]
print(a)
print(b)
for i in range(len(a)):
    if a[i]!="":
        ma=b[i]
        for j in range(i+1,len(a)):
            if str(a[i])!="" and a[j]==a[i]:
                ma = max(ma,b[i])
        print(a[i]," ",ma)
        a[i] =""
        