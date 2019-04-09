# 2.5 查找和替换文本
# 问题：对字符串中的文本做查找和替换
# 解决方案：简单的文本模式，使用str.replace()
#         复杂的文本模式，使用re.sub()函数
#         更复杂的情况，使用替换回调函数

# 简单查找替换：
text1 = 'yeah, but no, but yeah, but no, but yeah'
print(text1.replace('yeah', 'yep'))
#  yep, but no, but yep, but no, but yep


# 使用re.sub()函数，替换日期格式
# sub()第一个参数为要被替换的格式，第二个参数代表要新的格式，数字代表第几个捕获组，第三个参数是字符串
# 也可以使用compile预编译正则表达式
import re

text2 = 'Today is 11/27/2012, Pycon starts 3/13/2013.'
s = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
print(s)
# Today is 2012-11-27, Pycon starts 2013-3-13.

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
s = datepat.sub(r'\3-\1-\2', text2)
print(s)

# 使用替换回调函数
# month_abbr：月份名称简称的数组，比如month_abbr[0]：Jan
# 替换回调函数的输入参数是一个match对象，由match或find()返回。用group()方法来提取匹配中特定的部分。
# 该函数返回替换后的文本。
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

s = datepat.sub(change_date, text2)
print(s)
# Today is 27 Nov 2012, Pycon starts 13 Mar 2013.

# re.subn()可以知道一共完成了多少次替换
newtext, n = datepat.subn(r'\3-\1-\2', text2)
print(newtext, 'n: ', n)
# Today is 2012-11-27, Pycon starts 2013-3-13. n:  2
