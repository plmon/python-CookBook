# 1.16 筛选序列中的元素

# 问题：筛选出序列中满足要求的值或对序列做删减
# 解决方案：
# 1. 使用列表推导式（list comprehension）
#              -----> 当输入很大时会产生很大的结果
# 2. 使用生成器表达式通过迭代的方法产生筛选的结果
# 3. 使用内建函数filter()
#              -----> 筛选条件很复杂时，可以单独写一个筛选函数然后使用filter()
# 扩展： itertools.compress()
# list()可以将一个迭代器变成一个列表

# 1. 使用列表推导式:
list1 = [1, 4, -35, 10, -7, 2, 3, -1]
a = [i for i in list1 if i > 0 ]
print(a)  # [1, 4, 10, 2, 3]

# 2. 使用生成器表达式:
b = (i for i in list1 if i > 0)
for item in b:
    print(item)  # 1 4 10 2 3

# 3. 使用内建函数filter:
list2 = ['1', '5', '-', '-3', 'N/A', '3', '2']


def is_int(var):
    try:
        x = int(var)
        return x
    except ValueError:
        return False


c = list(filter(is_int, list2))
print(c)      # ['1', '5', '-3', '3', '2']

# 列表推导式和列表生成器可以同时对数据做转换：
import math
d = [math.sqrt(i) for i in list1 if i > 0]
print(d)      # [1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

# 新值替换旧值，替换掉某些不符合标准的值
f = [n if n > 0 else 0 for n in list1]
print(f)      # [1, 4, 0, 10, 0, 2, 3, 0]
g = [n if n < 0 else 0 for n in list1]
print(g)      # [0, 0, -35, 0, -7, 0, 0, -1]

# 筛选工具itertools.compress()：接受一个可迭代对象和一个布尔选择器序列作为输入
# 输出时，给出所有在相应布尔选择器中为True的可迭代对象，返回一个迭代器
# 用处：把一个序列的筛选结果施加到另一个相关的序列上
from itertools import compress
address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVLLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [i > 5 for i in counts]
print(more5)    # [False, False, True, False, False, True, True, False]
h = list(compress(address, more5))
print(h)        # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']

