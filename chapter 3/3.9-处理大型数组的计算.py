# 3.9 处理大型数组的计算

# 目标：对大型数据集比如数组或网格（grid）进行计算
# 解决方案：涉及数组的计算密集型任务使用NumPy库
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z1 = x * 2
print(z1)   # [1, 2, 3, 4, 1, 2, 3, 4]

# z2 = x + 10   # 报错，只能连接List类型
z3 = x + y
print(z3)  # [1, 2, 3, 4, 5, 6, 7, 8]

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
az1 = ax * 2
print(az1)  # [2 4 6 8]

az2 = ax * 10
print(az2)  # [10 20 30 40]

az3 = ax + ay
print(az3)  # [ 6  8 10 12]

az4 = ax * ay
print(az4)  # [ 5 12 21 32]

# numpy提供一些通用操作可以直接对数组进行操作：
r1 = np.sqrt(ax)
print(r1)   # [1.         1.41421356 1.73205081 2.        ]

r2 = np.cos(ax)
print(r2)   # [ 0.54030231 -0.41614684 -0.9899925  -0.65364362]

# numpy在内存中是大块的连续内存，由同一种类型的数据组成。
# 因此numpy可以创建非常大的数组
grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)
# [[0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  ...
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]]

# numpy可以对数组进行索引和通用计算
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# 输出第一行
print(a[1])   # [5 6 7 8]

# 输出第一列
print(a[:, 1])  # [ 2  6 10]

# 输出对应的行和列，第一个参数为行，第二个参数为列
print(a[1:3, 1:3])
# [[ 6  7]
#  [10 11]]

a[1:3, 1:3] += 10
print(a)
# [[ 1  2  3  4]
#  [ 5 16 17  8]
#  [ 9 20 21 12]]

# 给每行加上相应的行向量
a += [100, 101, 102, 103]
print(a)
# [[101 103 105 107]
#  [105 117 119 111]
#  [109 121 123 115]]

# np.where(condition, a, b) ：如果condition条件成立，输出a，否则输出b：
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = np.where(a<10, a, 10)
print(b)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 10 10]]
