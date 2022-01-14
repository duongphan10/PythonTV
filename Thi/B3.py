import numpy as np
import random
import math

a = np.array([np.random.randint(2,9) for i in range(9)]).reshape(3, 3)
b = np.array([np.random.randint(10,20) for i in range(9)]).reshape(3, 3)
# print(a)
# print(b)
c = a.dot(b)
ma = 0
sum =0
for i in range(3):
    for j in range(3):
        ma = max(ma,c[i][j])
        sum+= c[i][j]
print(c)
print("Phần tử lớn nhất: ",ma)
print("Trung bình cộng: ",sum/9)
