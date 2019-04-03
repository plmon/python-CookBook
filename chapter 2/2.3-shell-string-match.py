# 2.3 利用shell通配符做字符串匹配

# 问题： 工作在UNIX Shell下时，想使用常见的通配符模式对文本进行匹配
# 解决方案： 使用fnmatch.fnmatch()或fnmatch.fnmatchcase()

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))  # True
print(fnmatch('foo.txt', '?oo.txt')) # True
names = ['dat1.csv', 'dat2.csv', 'dat3.csv', 'foo.py', 'config.ini']
n = [name for name in names if fnmatch(name, 'dat*.csv')]
print(n)
# ['dat1.csv', 'dat2.csv', 'dat3.csv']

# 不同的操作系统匹配模式不同，fnmatch的结果随所使用的操作系统操作改变
# 若要求保持区别，可以使用fnmatchcase()，可以根据自己提供的大小写方式来匹配