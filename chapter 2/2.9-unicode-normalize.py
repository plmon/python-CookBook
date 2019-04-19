# 2.9 将Unicode文本统一表示为规范形式

# 目标：所有的字符串都有相同的底层表示
# 解决方案： unicodedata.normalize()方法

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print('s1:', s1, 's2:', s2)       # s1: Spicy Jalapeño s2: Spicy Jalapeño
print(s1 == s2)                   # False
print(len(s1), len(s2))           # 14 15

# 使用unicodedata.normalize()方法统一字符：
# 第一个参数指定字符串如果完成规范化表示。
# NFC表示字符应该是圈组成，NFD表示使用组合字符，即每个字符应该是能完全分开的
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)              # True
print(ascii(t1))             # 'Spicy Jalape\xf1o'

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)              # True
print(ascii(t3))             # 'Spicy Jalapen\u0303o'

# NFKC和NKFD规范表示形式,为处理特定类型的字符增加了额外的兼容内容：
s = '\ufb01'
print(s)                     # ﬁ
z1 = unicodedata.normalize('NFD', s)
print(z1)                    # ﬁ
z2 = unicodedata.normalize('NFKD', s)
print(z2)                    # fi
z3 = unicodedata.normalize('NFKC', s)
print(z3)                    # fi
