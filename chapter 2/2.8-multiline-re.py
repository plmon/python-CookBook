# 2.8 编写多行模式的正则表达式
# . 只能匹配除换行符外的任意字符，因此不能匹配多行，可以自定义对换行符的支持
# re.DOTALL可以设定 . 匹配任意的字符，包括换行符

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = ' /* this is a comment . */ '
text2 = '''   /* this is a 
                    multine comment*/  
        '''

comment_text1 = comment.findall(text1)
print(comment_text1)
# [' this is a comment . ']
comment_text2 = comment.findall(text2)
print(comment_text2)
# []

# 自定义对换行符的支持    ?:是只去掉（）的优先显示
multiline_comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment_text2_multiline = multiline_comment.findall(text2)
print(comment_text2_multiline)
# [' this is a \n                    multine comment']

# re.DOTALL
dotall_comment = re.compile(r'/\*(.*)\*/', flags=re.DOTALL)
comment_text2_DOTALL = dotall_comment.findall(text2)
print(comment_text2_DOTALL)
# [' this is a \n                    multine comment']
