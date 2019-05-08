# 3.8 分数的计算

# 目标：处理分数
# 解决方案：fractions模块
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
x1 = a + b
print(x1)  # 27/16

x2 = a * b
print(x2)  # 35/64

# 获取分子
print(x2.numerator)  # 35

# 获取分母
print(x2.denominator)  # 64

# 转换分数为浮点数
x3 = float(x2)
print(x3)   # 0.546875

# 限制转换后分母的最大值
x4 = x2.limit_denominator(8)
print(x4)  # 4/7

# 将浮点数转化为分数
c = 3.75
x5 = Fraction(*c.as_integer_ratio())   # *
print(x5) # 15/4
x6 = Fraction(c)
print(x6)  # 15/4
x7 = c.as_integer_ratio()
print(x7)  # (15, 4)
