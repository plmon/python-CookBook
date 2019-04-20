# 2.14 字符串连接及合并

# 目标：将小字符串合并成一个大的字符串
# 解决方案：join()方法、'+'方法、format()方法、yield()方法

# join()：
# 如果要合并的字符串在一个序列或可迭代对象中，那么将他们合并起来的最快方法就是使用join()：
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s1 = ' '.join(parts)
print(s1)             # Is Chicago Not Chicago?
s2 = ','.join(parts)
print(s2)             # Is,Chicago,Not,Chicago?
s3 = ''.join(parts)
print(s3)             # IsChicagoNotChicago?

# '+'方法：
a = 'Is Chicago'
b = 'Not Chicago?'
s4 = a + ' ' + b
print(s4)             # Is Chicago Not Chicago?

# '+'代替format()方法(s5同s4比较)：
s5 = '{} {}'.format(a, b)
print(s5)             # Is Chicago Not Chicago?

# 可以简单的将字面值合并在一起
s6 = 'Hello' 'World'
print(s6)             # HelloWorld

# 讨论：'+'方法会产生很多临时对象，增加内存空间，效率降低
# 大量的短词组结合，用'+'方法效率很低，不如用join()方法
# 也可以使用yield生成器，提高效率
data = ['ACME', 50, 91.1]
s7 = ''.join(str(d) for d in data)
print(s7)             # ACME5091.1

# 三种打印字符串的写法比较：
a = 'a'
b = 'b'
c = 'c'
print(a + ':' + b + ':' + c)  # ugly
print(':'.join([a, b, c]))      # Still ugly
print(a, b, c ,sep=':')       # Better

# 使用yiled生成器：
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        # print(part)
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 3):
    print(part)
# IsChicago
# IsChicago

for part in combine(sample(), 500):
    print(part)
# IsChicagoNotChicago?

# combine()第二个参数为控制字符串的长度，如果超过规定长度就输出目前字符串的合并