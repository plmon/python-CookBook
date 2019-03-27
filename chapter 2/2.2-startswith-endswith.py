# 2.2 在字符串的开头或结尾处做文本匹配

# 问题：在字符串的开头或结尾处按照指定的文本模式做检查，
#      例如检查文件的扩展名、URL协议类型等。
# 解决方案： 使用str.startswith()和str.endswith()
#          startswith()和endswith()可以传入多个可能选项，但是要使用元组结构。
#          也可以使用正则表达式，有点大材小用
# 主要用处：改进使用切片对字符串分割，代码整洁美观轻便

filename = 'spam.txt'
ends = filename.endswith('.txt')
starts = filename.startswith('file:')
print(ends, starts)   # True False

filename = ['a.c', 'a.h', 'b.c', 'b.py', 'java']
file = [f for f in filename if f.endswith(('.c', '.h'))]
print(file)  # ['a.c', 'a.h', 'b.c']
a = any(name.endswith('py') for name in filename)
print(a)     # True

# 如果不为元组输入会报错，比如：
# file2 = [f for f in filename if f.endswith(['.c', '.h'])]
# TypeError: endswith first arg must be str or a tuple of str, not list
