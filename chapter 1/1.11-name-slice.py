# 对切片命名可以解决难懂的硬编码索引问题
# 通过切片有效的名称可以在日后回顾代码时一目了然
record = '123456789...100......5123.25...'

# 硬编码切片，难以读懂什么意思
cost1 = int(record[12:15]) * float(record[21:28])

# 对切片进行命名，可以清楚的知道切片的含义
shares = slice(12, 15)
price = slice(21, 28)
cost2 = int(record[shares]) * float(record[price])  # 100 * 512325.0

# 可以使用start stop step属性获得slice实例的信息：
a = slice(2, 6, 2)
b = slice(2, 6)
print(a.start, a.stop, a.step)  # 2, 6, 2
print(b.start, b.stop, b.step)  # 2, 6, None  步长为None

# s.indice(n) 相当于构造一个0-n的矩阵，然后应用s的slice()
s = "helloworld"
print(a.indices(len(s)))  # (2,6,2)
print(b.indices(len(s)))  # (2,6,1)  如果切片未定义步长，默认为1
for i in range(*a.indices(len(s))):
    print(i)      # 2 4
    print(s[i])   # l o
for i in range(*b.indices(len(s))):
    print(s[i])   # l l o w

print(*a.indices(len(s)))  # [2, 6, 2]   *--是列表


