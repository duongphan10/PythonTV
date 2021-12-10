import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#đọc file csv
df = pd.read_csv("Social_Network_Ads_2.csv")

df1 = df.copy()
#Thay tên cột "Purchased"
df1=df1.rename(columns = {"Purchased":'Status'}) 
#Thay đổi giá trị ứng với 0 or 1 
df1['Status'] = df1['Status'].map({0 :"Chưa mua", 1: "Đã mua"})




