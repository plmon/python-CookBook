# 2.11 从字符串中去掉不需要的字符

# 目标：去掉字符串开始、结尾或中间不需要的字符。
# 解决方案：strip()、replace()、re.sub()
s = '  hello     world  '
print(s.strip())   # 'hello     world'
print(s.lstrip())  # 'hello     world  '
print(s.rstrip())  # '   hello     world'

t = '-----hello world====='
print(t.lstrip('-'))       # 'hello world====='
print(t.rstrip('='))       # '-----hello world'
print(s.replace(' ', ''))  # 'helloworld'

import re
print(re.sub(r'\s+', ' ', s))   # ' hello world '

