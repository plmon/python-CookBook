# 1.15 根据字段将记录分组

# 问题：有一系列的字典或对象实例，根据其中的某个特定的字段将数据分组。
# 解决方案：
# 1. 先将序列按照字段顺序排序，然后使用itertools.groupby()
# 2. 使用collections.defaultdict()创建一个一键多值字典
#                  ------>  占用内存，但是速度比先排序后分组快

from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVLLE', 'date': '07/04/2012'},
]

# 1. sort + groupby()：
# groupby()创建了一个迭代器，在每次迭代时返回一个值和一个子迭代器
# 值为分组的值，
# 子迭代器可以产生所有在该分组内具有该值的项。
# 使用groupby()需要事先对列表进行排序，groupby()只能检查连续的项。
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# output
# 07/01/2012
#   {'address': '5412 N CLARK', 'date': '07/01/2012'}
#   {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
# 07/02/2012
#   {'address': '5800 E 58TH', 'date': '07/02/2012'}
#   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
#   {'address': '1060 W ADDISON', 'date': '07/02/2012'}
# 07/03/2012
#   {'address': '2122 N CLARK', 'date': '07/03/2012'}
# 07/04/2012
#   {'address': '5148 N CLARK', 'date': '07/04/2012'}
#   {'address': '1039 W GRANVLLE', 'date': '07/04/2012'}


# 2. 一键多值defaultdict()，不用排序，将数据放入数据结构中，允许进行随机访问：
d = defaultdict(list)
for i in rows:
    d[i['date']].append(i)

for r in d['07/01/2012']:
    print(r)

# output:
# {'address': '5412 N CLARK', 'date': '07/01/2012'}
# {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
