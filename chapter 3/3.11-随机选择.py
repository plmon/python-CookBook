# 3.11 随机选择

# 目标：从序列中随机挑选出元素，或者生成随机数
# 解决方案： random模块

# 从序列中随机挑选出元素，使用random.choice()
import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))  # 2
print(random.choice(values))  # 1
print(random.choice(values))  # 2
print(random.choice(values))  # 5
print(random.choice(values))  # 2

# 取样N个元素，将选出的元素移除做进一步考察，使用random.sample()：
print(random.sample(values, 2))  # [2, 3]
print(random.sample(values, 2))  # [2, 6]
print(random.sample(values, 3))  # [5, 1, 6]
print(random.sample(values, 3))  # [1, 5, 3]

# 随机打乱元素顺序（洗牌），使用random.shuffle()：
random.shuffle(values)
print(values)   # [1, 5, 3, 4, 2, 6]
random.shuffle(values)
print(values)   # [2, 6, 1, 3, 4, 5]

# 产生随机整数，使用random.randint():
print(random.randint(0, 10))  # 2
print(random.randint(0, 10))  # 9
print(random.randint(0, 10))  # 4

# 产生0-1之间均匀分布的浮点数值，使用random.random()：
print(random.random())  # 0.7932779365019395
print(random.random())  # 0.46562013918916556
print(random.random())  # 0.861439267366276

# 产生N个随机比特位表示的整数，使用random.getrangbits()：
print(random.getrandbits(20))  # 576662

# 改变random的初始种子使用random.seed()方法
