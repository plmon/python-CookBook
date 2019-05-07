# 3.5 从字节串中打包和解包大整数

# 目标：有一个字节串，需要将其解包为一个整数。同时，讲一个大整数重新转化为字节串。
# 解决方案：int.from_bytes()、int.to_bytes()

data = b'\x00\x124v\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
length = len(data)
little_data = int.from_bytes(data, 'little')   # 小端序
print(little_data)
# 69120565665751139577663547927631761920

big_data = int.from_bytes(data, 'big')    # 大端序
print(big_data)
# 94525377821947740945920721189797940

data1 = big_data.to_bytes(length, 'big')
print(data1)
# b'\x00\x124v\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

data2 = big_data.to_bytes(length, 'little')
print(data2)
# b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00v4\x12\x00'

