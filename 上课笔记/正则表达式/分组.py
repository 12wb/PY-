import re
'''
def compile(pattern,flags=0)
def match(patter,atring flags=0)

i = re.compile('\d+',re.I)
# 这个是爬数字的
s = i.match('12354323432')
sl = i.findall('assd')
'''


te1 = '0731-82869005'

yanzheng = re.match(r'(\d{4})-(\d{8})$',te1)
print(yanzheng)
print(yanzheng.group())
print(yanzheng.group(1))
print(yanzheng.group(2))


