# 1.12 找出序列中出现次数最多的元素

# 使用collections模块中的Counter类

from collections import Counter

words = ['a', 'b', 'c', 'a', 'd', 'a', 'e', 'b', 'a', 'c', 'b', 'c', 'e']

# 创建Counter对象，Counter底层实现为一个字典
# key为单词，value为对应单词的数量
word_counts = Counter(words)
print(word_counts)  # Counter({'a': 4, 'b': 3, 'c': 3, 'e': 2, 'd': 1})

# 输出数量排名前三的单词和对应的次数
top_three = word_counts.most_common(3)
print(top_three)    # [('a', 4), ('b', 3), ('c', 3)]

# 在当前序列的基础上在新增一个序列，使用update方法
more_words = ['a', 'g', 'b', 'f', 'c', 'a', 'b']
word_counts.update(more_words)
print(word_counts)   # Counter({'a': 6, 'b': 5, 'c': 4, 'e': 2, 'd': 1, 'g': 1, 'f': 1})

# Counter可以同数学运算公式结合起来使用，比如：
a = Counter(words)
print(a)             # Counter({'a': 4, 'b': 3, 'c': 3, 'e': 2, 'd': 1})
b = Counter(more_words)
print(b)             # Counter({'a': 2, 'b': 2, 'g': 1, 'f': 1, 'c': 1})
c = a + b
print(c)             # Counter({'a': 6, 'b': 5, 'c': 4, 'e': 2, 'd': 1, 'g': 1, 'f': 1})

d = a - b
print(d)             # Counter({'a': 2, 'c': 2, 'e': 2, 'b': 1, 'd': 1})