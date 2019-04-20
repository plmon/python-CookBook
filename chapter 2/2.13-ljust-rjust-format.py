# 2.13 对齐文本字符串

# 目标：将文本对齐
# 解决方案：rjust()、ljust()、center()、format()

# ljust、rjust、center函数分别是左对齐、右对齐和居中
# s.ljust(width, token)有两个参数，
# 第一参数为将字符串补充为长度为width的字符串，
# 第二个参数为补充的字符,默认为空格
text = 'hello world'
ltext = text.ljust(20)
print(ltext)             # 'hello world         '
rtext = text.rjust(20)
print(rtext)             # '         hello world'
r_text = text.rjust(20, '-')
print(r_text)            # '---------hello world'
ctext = text.center(20)
print(ctext)             # '    hello world     '
c_text = text.center(20, '*')
print(c_text)            # '****hello world*****'

# format()函数也可以对齐字符串，利用<|>|^三个符号，分别为左对齐、右对齐和居中
f1 = format(text, '<20')
print(f1)                # 'hello world         '
f2 = format(text, '>20')
print(f2)                # '         hello world'
f3 = format(text, '^20')
print(f3)                # '    hello world     '
f4 = format(text, '=>20')
print(f4)                # '=========hello world'

# format格式化多个值
f5 = '{:>10s} {:>10s}'.format('Hello', 'World')
print(f5)                # '    Hello      World'

# format也可以用在多种类型的值上，比如：
x = 1.2345
f6 = format(x, '>10')
print(f6)                # '    1.2345'
f7 = format(x, '^10.2f')
print(f7)                # '   1.23   '
