import re
'''
def match(pattern,string,flags=0)
全字符匹配，并输出第一个匹配值。
参数用法和match一样。
'''
i = re.search('hello ','Hello ,world! hello ,sunshine!',re.I)  # 忽略大小写 re.I可以匹配输出大写的Hello
print(i)
print(i.group())

'''
def findall(pattern,string,flags=0)
找到所有匹配对象
返回所有对象列表
fiags = ? 输出某个对象
'''
patter = re.compile(r'\d+')  # \d匹配任意数字，等价于[0到9]
s = patter.findall('run22ogg123google789',0,10)
print(s)