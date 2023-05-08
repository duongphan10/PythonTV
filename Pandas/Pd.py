import pandas as pd
d = {   "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
        "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),}
# Tạo DataFrame 
df = pd.DataFrame(d)

# thêm cột bốn với giá trị mỗi ô theo công thức
df["three"] = df["one"] * df["two"]

# thêm cột True/False theo điều kiện
df["flag"] = df["one"] > 2

# thêm cột với giá trị vô hướng (scalar value)
df["foo"] = "bar"

# thêm cột không cùng số lượng index với DataFrame
df["one_trunc"] = df["one"][:2]

# dùng hàm insert. Cột "bar" bên dưới sẽ ở vị trí 1 (tính từ 0), có giá trị bằng cột "one"
df.insert(1, "bar", df["one"])

# Output:
#    one  bar  two  three   flag  foo  one_trunc
# a  1.0  1.0  1.0    1.0  False  bar        1.0
# b  2.0  2.0  2.0    4.0  False  bar        2.0
# c  3.0  3.0  3.0    9.0   True  bar        NaN
# d  NaN  NaN  4.0    NaN  False  bar        NaN

# Xóa cột "two"
del df["two"]

# pop cột three với dict three
three = df.pop("three")

print(df)
# Output:
#    one  bar   flag  foo  one_trunc
# a  1.0  1.0  False  bar        1.0
# b  2.0  2.0  False  bar        2.0
# c  3.0  3.0   True  bar        NaN
# d  NaN  NaN  False  bar        NaN

# chọn dòng theo label
df.loc["b"] 
# one            2.0
# bar            2.0
# flag         False
# foo            bar
# one_trunc      2.0
# Name: b, dtype: object

# chọn dòng theo vị trí nguyên
df.iloc[2]
# one           3.0
# bar           3.0
# flag         True
# foo           bar
# one_trunc     NaN
# Name: c, dtype: object

# cắt lấy ra từ dòng 2 đến dòng 3
d = df[1:3]
#    one  bar   flag  foo  one_trunc
# b  2.0  2.0  False  bar        2.0
# c  3.0  3.0   True  bar        NaN

#    one  bar   flag  foo  one_trunc
# a  1.0  1.0  False  bar        1.0
# b  2.0  2.0  False  bar        2.0
# c  3.0  3.0   True  bar        NaN
# d  NaN  NaN  False  bar        NaN

# Ghi file DataFrame ra tệp csv 
#df.to_csv(r'pandas.csv',index= None, header=None)

