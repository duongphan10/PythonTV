import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.subplot(2,1,1)
#đọc file csv
mall = pd.read_csv("Mall_Customers_2.csv")
#Lưu list màu tùy với giới tính
color = ["blue" if i == "Male" else "pink" for i in mall["Genre"]]
#Vẽ biêu đồ phân tán
plt.scatter(mall["Age"],mall["Spending Score (1-100)"],c=color)
#Tên các côt 
plt.xlabel("Tuổi")
plt.ylabel("Chi Tiêu")

plt.subplot(2,1,2)
# Lưu các dữ liệu sang list 
Age = mall["Age"]
Mon = mall["Annual Income (k$)"]
# Các thao tác tính thu nhập trung bình theo tuổi
X = []  # Mảng lưu tuổi
Y = []  # Mảng lưu thu nhập theo tuổi
s =0 
x=0
for i in range(0,100):
    sum=0
    dem = 0
    for j in range(len(Age)):
        if Age[j]== i:
            sum+=Mon[j]
            dem+=1
    if dem!=0: 
        X.append(i)
        Y.append(sum/dem)
        if sum/dem>s:
            s=sum/dem
            x=i
# Vẽ biêủ đồ đường theo tuổi và thu nhập trung bình hằng năm 
plt.plot(X,Y);
# Vẽ mũi tên vị trí tuổi có thu nhập cao nhất 
plt.annotate('MAX',xy=(x,s),xytext=(x+4,s+4),arrowprops=dict(facecolor='green'));
plt.xlabel("Tuổi")
plt.ylabel("Thu Nhập Hằng Năm")
plt.show()

