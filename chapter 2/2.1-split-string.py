# 2.1 针对任意多的分隔符拆分字符串

# 问题：将字符串拆分成不同的字段，但是分隔符在整个字符串中可能不一致
# 解决方案：使用re.split()方法

import re
line = 'adsg fjdk; afed, fjek,asdf,   foo'
str1 = re.split(r'[;,\s]\s*', line)    # 正则表达式
print(str1)   # ['adsg', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 如果正则表达式中使用到了捕获组，那么匹配到的文本也会包含在最终结果中：
str2 = re.split(r'(;|,|\s)\s*', line)
print(str2)   # ['adsg', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

# 可以获取分割字符，用在之后要用到分割字符的地方,恢复原始字符串：
values = str2[::2]
delimiters = str2[1::2] + ['']
str3 = ''.join(v+d for v, d in zip(values, delimiters))
print(values)  # ['adsg', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print(delimiters)  # [' ', ';', ',', ',', ',', '']
print(str3)    # adsg fjdk;afed,fjek,asdf,foo

# 非捕获组的表达方式 (?:...) ，如下：
str4 = re.split(r'(?:;|,|\s)\s*', line)
print(str4)    # ['adsg', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
