# 3.13 计算上周五的日期

# 目标：找出一周中上一次出现某天时的日期。比如：上周五是几月几号
# 解决方案：

# datetime模块编写函数
from datetime import datetime, timedelta

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def previous_week_day(dayname, start_time = None):
    if start_time is None:
        start_time = datetime.today()

    day_num = start_time.weekday()
    day_num_target = week.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7

    target_date = start_time - timedelta(days=days_ago)

    return  target_date


print(previous_week_day('friday'))   # 2019-05-03 20:36:49.257763

# 使用dateutil.relativedelta函数，一句话就可以完成：
# 有相关缺陷，输入当天星期时，输出仍为当天日期：
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)   # 2019-05-10 20:36:49.278707

# 输出下一星期一时间
r = d + relativedelta(weekday=MO)
print(r)   # 2019-05-13 20:37:58.745005

# 输出上一星期星期一时间
r = d + relativedelta(weekday=MO(-1))
print(r)   # 2019-05-06 20:37:58.745005

# 今天为周五，输入为周五时，时间仍为今天
r = d + relativedelta(weekday=FR(-1))
print(r)   # 2019-05-10 20:39:55.955634

r = d + relativedelta(weekday=FR)
print(r)   # 2019-05-10 20:39:55.955634