# 1.20 将多个映射合并为单个映射

# 问题：将多个字典或映射逻辑上合并为一个单独的映射结构
# 解决方案：
# 1. 使用collections.ChainMap类
# 2. 使用字典的update()方法

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 使用collections.ChainMap类：修改映射的操作会作用在列出的第一个映射结构上。
from collections import ChainMap
c = ChainMap(a, b)
print(c['x'], c['y'], c['z'])   # 1 2 3
c['z'] = 10
c['w'] = 25
del c['x']
del c['y']      # KeyError: "Key not found in the first mapping: 'y'"   //a字典中没有'y'，显示错误
print(a)   # {'z': 10, 'w': 25}
print(b)   # {'y': 2, 'z': 4}
print(c)   # ChainMap({'z': 10, 'w': 25}, {'y': 2, 'z': 4})

# ChainMap
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
values = values.new_child()
print(values)  # ChainMap({}, {'x': 3}, {'x': 2}, {'x': 1})

values = values.parents
print(values['x'])  # 3
values = values.parents
print(values['x'])  # 2

# 使用update方法：需要单独构造一个完整的字典对象，或修改现有的字典。
# 如果其中任何一个原始字典做了修改，不会反应到合并后的字典中。
# 但是ChainMap使用的是原始的字典，修改后反映到原始的字典中：
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged)  # {'y': 2, 'z': 3, 'x': 1}
a['x'] = 13
print(merged['x'])   # 1   //未修改回原有的字典



