# 1.14 对不原生支持比较操作的对象排序
# 目的：对不能进行比较操作的同一个类的实例进行排序
# 方法：利用sorted()和operator.attrgetter()结合进行排序
#      该方法同时可用于max()和min()函数
#      attrgetter()相当于创建了一个函数，然后将函数作用于对象上
# 用处：创建同一个类的许多实例，想要对它们之间进行排序操作时

from operator import attrgetter


class Users:
    def __init__(self, user_id):
        self.user_id = user_id

    # 格式化类输出信息
    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [Users(23), Users(3), Users(99)]
a = sorted(users, key=attrgetter('user_id'))
print(a)    # [User(3), User(23), User(99)]

# 也可以使用lambda表达式，但是性能不好
b = sorted(users, key=lambda k: k.user_id)
