import re
'''
任意合法字符
[0-9],[12345] 字符集合表示
[0-9 a-z A-Z] 所有数字，大小写字母
\d 匹配数字
\w 匹配[0-9a-zA-Z]
\W 除了\w之外的集合
^ 取反
[^abc] 匹配abc的非集合，^我们称为脱字符
^'abc' 匹配字符串的首位为abc
'abc$' 匹配字符串尾位为abc
'''

print(re.search('.[0-9a-zA-Z].','kp_'))

print(re.search('^hello','good man,hello'))

# print(re.search('^[A-Z]'))