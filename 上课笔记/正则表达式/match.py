import re
# def match(pattern,string,flags=0)
# pattern 正则表达式
# flags 补充匹配的规则re.I,re.W   flags作用于pattern
'''
i = re.match('人工智能3182','人工智能3182 3183')  # 从前往后逐一匹配,只要第一个没有匹配成功，后面则不匹配
print(i)
print(i.group())  #i.group()输出文本
# i.start(),i.end(),i.span()
'''

i = re.match('abc','abcdre')
print(i.group())  # 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。
print(i.start())  # 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。
print(i.end())  # 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。
print(i.span())  # 返回(start(group), end(group))。
i = re.match('abc','dreabc')
print(i)

i = re.match('人工智能318[0-9]','人工智能3189')
print(i)
print(i.group())  #i.group()输出文本
