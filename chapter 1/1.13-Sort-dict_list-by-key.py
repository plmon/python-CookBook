# 1.13 通过公共键对字典列表排序
# 目的：根据字典列表中的值对字典列表进行排序
# 方法：利用operator.itemgetter()和sorted()对具有公共字段的字典进行排列
#      该方法同时适用于mix()和max()函数。
# 用处：用于数据库或数据处理中


# 使用itemgetter()
from operator import itemgetter

member = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

member_by_fname = sorted(member, key=itemgetter('fname'))
print(member_by_fname)
# [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
member_by_uid = sorted(member, key=itemgetter('uid'))
print(member_by_uid)
# [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]


# itemgetter()可以接受多个键
member_by_lfname = sorted(member, key=itemgetter('lname', 'fname'))
print(member_by_lfname)
# [{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]

# 可用lambda表达式进行排列，但是性能不如itemgetter好。
member_by_fname_lambda = sorted(member, key=lambda k: k['fname'])
member_by_lfname_lambda = sorted(member, key=lambda k: (k['lname'], k['fname']))
