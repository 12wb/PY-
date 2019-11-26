import re
email = input('请输入用户名：')
i = re.search(r'\w{1,22}@163.com',email)
print(i)
print(i.group())