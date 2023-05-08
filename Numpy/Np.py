import numpy as np
import random

# Khởi tạo mảng 
array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

a = np.zeros(shape=(3,3,3), dtype= int)     # Khởi tạo mảng vơi các phần tử bằng 0

b = np.full(shape=(3,3), fill_value= 2)     # Khởi tạo mảng với giá trị bất kì

c = np.random.randint(0,10)
d = random.randint(0,10)
f = np.full(shape=(random.randint(1,4),random.randint(0,5)), fill_value=np.random.randint(1,10))
# print(f.shape)
# print(f)
e = np.array([[1,2,3,4,5],
             [6,7,8,9,10]])
# print(e.shape)
# print(e.reshape(1,e.shape[1]*2))
# print(e.shape[0] * e.shape[1])
# print(e.size)
# print(e.ndim)   # Số chiều của ma trận
# print(e[1][2:4])

load_file = np.array([np.loadtxt(fname='Text.txt',dtype= int)])
print(load_file[0,6])