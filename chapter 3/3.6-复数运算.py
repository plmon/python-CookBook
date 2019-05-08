# 3.6 复数运算

# 解决方案：通过complex(real, imag)函数来指定复数，或通过浮点数加上后缀j来指定。
a = complex(2, 4)
b = 3 - 5j
print(a)   # (2+4j)
print(b)   # (3-5j)

print(a.real)   # 2.0
print(a.imag)   # 4.0
c = a.conjugate()    # 共轭复数
print(c)        # (2-4j)

# 运算操作可以作用在复数上
x1 = a + b
print(x1)       # (5-1j)
x2 = a * b
print(x2)       # (26+2j)
x3 = a / b
print(x3)       # (-0.4117647058823529+0.6470588235294118j)
x4 = abs(a)
print(x4)       # 4.47213595499958

# 有关复数的函数操作可以使用cmath模块,math模块不会使用复数，也不支持复数操作：
import cmath
y1 = cmath.sin(a)
print(y1)       # (24.83130584894638-11.356612711218174j)
y2 = cmath.cos(a)
print(y2)       # (-11.36423470640106-24.814651485634187j)
y3 = cmath.exp(a)
print(y3)       # (-4.829809383269385-5.5920560936409816j)

# Python中大部分和数学相关的模块都可用于复数，比如numpy模块：
import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])   # 复数数组
print(a)        # [2.+3.j 4.+5.j 6.-7.j 8.+9.j]
b = a + 2
print(b)        # [ 4.+3.j  6.+5.j  8.-7.j 10.+9.j]
c = np.sin(a)
print(c)        # [   9.15449915  -4.16890696j  -56.16227422 -48.50245524j -153.20827755-526.47684926j 4008.42651446-589.49948373j]
