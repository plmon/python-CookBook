# 2.6 以不区分大小写的方式对文本做查找和替换
# 问题：以不区分大小写的方式在文本中进行查找，可能还需要做替换
# 解决方案： 使用re.IGNORECASE标记和支撑函数
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
s1 = re.findall('python', text, flags=re.IGNORECASE)
print(s1)
# ['PYTHON', 'python', 'Python']
s2 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(s2)
# UPPER snake, lower snake, Mixed snake

# 从上面可以看到替换的结果不会匹配原始的字符的大小写，因此写一个支撑函数：
def matchcase(word):
    def replace(m):
        print(m)
        text = m.group()
        print(text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


s = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(s)
# UPPER SNAKE, lower snake, Mixed Snake