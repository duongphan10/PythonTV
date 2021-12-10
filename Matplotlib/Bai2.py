import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

#đọc file csv
df = pd.read_csv("Social_Network_Ads_2.csv")
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
df.iloc[:, 1:3] = imp.fit_transform(df.iloc[:, 1:3])

df1 = df.copy()
#Thay tên cột "Purchased"
df1=df1.rename(columns = {"Purchased":'Status'}) 
#Thay đổi giá trị ứng với 0 or 1 
df1['Status'] = df1['Status'].map({0 :"Chưa mua", 1: "Đã mua"})


Age = df1['Age']
Sta = df1['Status']
Sal = df['EstimatedSalary']
color = ['red' if i == 'Chưa mua' else 'green' for i in Sta]

plt.figure(figsize=(10,5))

#vẽ biểu đồ cột
for i in range(len(color)) :
    plt.bar(Age[i], Sal[i], color = color[i])

plt.xlabel("Age")
plt.ylabel("EstimatedSalary")
plt.show()


#---------
# Tạo mảng màu cho Trạng thái đã mua hoặc Chưa mua tương ứng
color = np.array(['violet' if i == 'Đã mua' else 'red' for i in df1['Status']])

# Vẽ biểu đồ scatter dựa trên giá trị của Tuổi và Lương
plt.scatter(df1['Age'].values, df1['EstimatedSalary'].values, c=color)

plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.show()



