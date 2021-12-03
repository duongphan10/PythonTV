import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv("categorical_data.csv")
print(df)

#Cách 1: missingdata bằng SimpleImpute
df1 = df.copy()
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
'''
SimpleImputer là một lớp học scikit hữu ích trong việc xử lý dữ liệu bị thiếu trong tập dữ liệu mô hình dự đoán.
Nó thay thế các giá trị NaN bằng một trình giữ chỗ được chỉ định. 
missing_values : Phần giữ chỗ missing_values được thay thế. Theo mặc định là NaN.
strategy: Dữ liệu sẽ thay thế các giá trị NaN từ tập dữ liệu.
'''
#Thay thế dữ liệu 
imputer = imputer.fit(df1.iloc[:,1:3])
df1.iloc[:,1:3] = imputer.transform(df1.iloc[:,1:3])
print("Sử dụng SimpleImputer: \n", df1)

# Cách 2: missingdata bằng tay
df2 = df.copy()
# Hàm tính giá trị trung bình
def Check(a) :
    sum = 0
    dem = 0
    for i in a :
        if i!= np.nan :
            sum+=i
            dem+=1
    if dem==0 : 
        return None
    return sum/dem
# Lưu giá trị trung bình các cột 
Age = Check(df1.age)
Salary = Check(df1.salary)

# Thay thế dữ liệu thiếu của từng cột với giá trị tb đã tính
df2['age'].fillna(value = Age , inplace =True )
df2['salary'].fillna(value = Salary , inplace = True)

print("Tính tay :\n " , df2)
