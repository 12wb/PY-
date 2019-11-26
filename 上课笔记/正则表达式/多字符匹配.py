import re
'''
x  x为单字符
x? 匹配一个或者0个x
x+ 匹配一个或无数个x
x* 匹配0个或无数个x
x(n,m) 匹配有限个x
x|y 匹配x或y
'''

print(re.findall('x?','xxxxxxxx'))
print(re.findall('x+','xxxxxxxx'))
print(re.findall('x*','xxxxxxxx'))
print(re.findall('x{,3}3'
                 'xxxxyyyyxx'))
print(re.findall('x|y','xxyyzzxyzxyz'))