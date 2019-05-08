# 3.7 处理无穷大和NaN

# 目标：对浮点数的无穷大、负无穷大和NaN(Not a number)进行判断测试
# 解决方案：
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)    # inf
print(b)    # -inf
print(c)    # nan

# 可以使用math.isinf()和math.isnan()函数判断：
import math
result = math.isinf(a)
print(result)   # True
result = math.isinf(b)
print(result)   # True
result = math.isnan(c)
print(result)   # True

# 无穷大值和nan在数学计算中会进行传播：
x = a + 45
print(x)   # inf

# 但是inf存在某些特定的操作会导致未定义的行为并产生nan的结果，nan则是所有情况都为nan：
y = a/a
print(y)   # nan
z = a + b
print(z)   # nan

# nan不会被判定为相等，因此唯一判断是否为nan的方式就是使用math.isnan()：
d = float('nan')
result = (c == d)
print(result)    # False
result = c is d
print(result)    # False
