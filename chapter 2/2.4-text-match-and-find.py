# 2.4 文本模式的匹配和查找

# py中正则表达式re模块的使用
# 主要函数：re.match()、re.findall()、re.finditer()、re.compile

import re

# re.compile、re.match
# 当想要重复使用同一个正则表达式模式时，可以将该模式预编译成一个模式对象
datepat = re.compile(r'\d+/\d+/\d+')
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
print(datepat.match(text1))   # <re.Match object; span=(0, 10), match='11/27/2012'>  //代表匹配成功
print(datepat.match(text2))   # None

# match()方法只匹配开头，findall方法可以匹配所有文本项
text = 'today is 11/27/2012. pycon starts 3/13/2013'
m = datepat.match(text)
all = datepat.findall(text)
print(all)   # ['11/27/2012', '3/13/2013']

# ()定义捕获组
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match(text1)
print(m.groups())           # ('11', '27', '2012')
print(m.group(0), m.group(1), m.group(2), m.group(3))  # 11/27/2012 11 27 2012
print(datepat2.findall(text))  # [('11', '27', '2012'), ('3', '13', '2013')]

# findall可以改成迭代的方法finditer
for m in datepat2.finditer(text):
    print(m.groups())

# output:
# ('11', '27', '2012')
# ('3', '13', '2013')