# 3.12 时间换算

# 目标：进行简单的时间转换工作，比如讲日转换成秒，小时转换成分钟等。
# 解决方案：datatime模块

from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)                  # 2
print(c.seconds)               # 37800
print(c.seconds/3600)          # 10.5
print(c.total_seconds()/3600)  # 58.5

# 表示特定的日期和时间：
from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))  # 2012-10-03 00:00:00

b = datetime(2012, 12, 21)
d = b - a
print(d.days)   # 89

now = datetime.today()
print(now)     # 2019-05-10 20:08:59.206043
print(now + timedelta(minutes=10))  # 2019-05-10 20:18:59.206043

# datetime模块可以处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)         # 2 days, 0:00:00
print((a - b).days)  # 2

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)  # 1