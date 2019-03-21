# 1.18 将名称映射到序列的元素中

# 问题：代码中通过位置（索引、下标）来访问列表或元组，代码难以阅读。
#                                 --->通过名称来访问元素
# 解决方案：  collections.namedtuple()命名元组
# 应用：从数据库中调用大型元组列表时可以使用
# 相似问题： 对切片命名：1.11

# 扩展：
# 1. 作为字典的替代
# 2. 作为简便的方法填充具有可选或缺失字段的命名元组，并对相应值做替换
# 3. 当定义高效的数据结构且将来会修改各种实例属性时，可以考虑定义一个使用__slots__的类（8.4节）

# 给namedtuple()提供一个类型名称和相应字段，返回一个可实例化的类，定义好字段传入值。
# 类似一个类实例，支持所有元组所支持的操作

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('abc@123.com', '2019.2.5')
print(sub)               # Subscriber(addr='abc@123.com', joined='2019.2.5')
print(type(sub))         # <class '__main__.Subscriber'>    是一个类实例

# 普通元组和命名元组比较：
# 普通元组：
def ori_tuple(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# 命名元组：
Stock = namedtuple('Stock', ['name', 'share', 'price'])
def named_tuple(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)   # *是列表
        total += s.share * s.price
    return total

# namedstuple可以替代字典，构造大型数据结构时，比字典更高效，但是值没有办法改变
# 更改属性可以使用_replace()方法实现，会创建全新的命名元组，并对相应的值做替换
s = Stock('ACME', 100, 123.45)
print(s)                  # Stock(name='ACME', share=100, price=123.45)
# s.share = 75   # 会报错：AttributeError: can't set attribute

s = s._replace(share=75)  # Stock(name='ACME', share=75, price=123.45)
print(s)

# namedtuple替换缺失字段
stock_prototype = Stock('', 0, 0)
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100}
print(a)                 # {'name': 'ACME', 'shares': 100}
b = {'name': 'ACME', 'price': '123.45'}
print(b)                 # {'name': 'ACME', 'price': '123.45'}
