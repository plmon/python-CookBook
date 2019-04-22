# 2.5 给字符串中的变量名做插值处理

# 目标：创建一个字符串，对其中嵌入的变量名称会以变量字符串值的形式替换掉
# 解决方案：format()函数、format_map()函数

s = '{name} has {n} messages.'
t1 = s.format(name='Guido', n=37)
print(t1)                      # Guido has 37 messages.

# 使用format_map()
name = 'Guido'
n = 37
print(vars())
t2 = s.format_map(vars())
print(t2)                      # Guido has 37 messages.

# vars()也可以使用在类实例上：
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
t3 = s.format_map(vars(a))
print(t3)                      # Guido has 37 messages.

# format()、format_map()没办法处理缺失值,可以使用__missing__方法：
# s.format(name='Guido')
# 输出错误：KeyError:
#     s.format(name='Guido')
# KeyError: 'n'

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(vars())
t4 = s.format_map(safesub(vars()))
print(t4)                   # Guido has {n} messages.

# 可以通过栈帧函数，将替换变量的过程隐藏在一个功能函数内：
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

n = 32
print(sub('Hello {name}'))                     # Hello Guido
print(sub('You have {n} message'))             # You have 37 message
print(sub('Your favorite color is {color}'))   # Your favorite color is {color}


# 其余插值处理方法：
# 1：
# t5 = '%(name) has %%(n) messages.' % vars()
# print(t5)
# 2:
import string
s = string.Template('$name has $n messages.')
t6 = s.substitute(vars())
print(t6)                                       # Guido has 37 messages.
