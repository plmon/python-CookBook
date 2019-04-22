# 2.16 以固定列数重新格式化文本

# 目标：有很长的字符串，将他们按照用户指定
# 解决方案：textwrap()

text = "hello everybody, this is a test text,\
how to use textwrap() function. \
let us use it for fun !"

import textwrap
s1 = textwrap.fill(text, 70)
print(s1)
# hello everybody, this is a test text,how to use textwrap() function.
# let us use it for fun !

s2 = textwrap.fill(text, 40)
print(s2)
# hello everybody, this is a test text,how
# to use textwrap() function. let us use
# it for fun !

# initial_indent：进行初始化
s3 = textwrap.fill(text, 40, initial_indent='aaa')
print(s3)
# aaahello everybody, this is a test
# text,how to use textwrap() function. let
# us use it for fun !

# subsequent_indent:除了第一行以外其他所有行进行初始化
s4 = textwrap.fill(text, 40, subsequent_indent='bbb')
print(s4)
# hello everybody, this is a test text,how
# bbbto use textwrap() function. let us
# bbbuse it for fun !

s4 = textwrap.fill(s3, 40, subsequent_indent='bbb')
print(s4)
# aaahello everybody, this is a test
# bbbtext,how to use textwrap() function.
# bbblet us use it for fun !