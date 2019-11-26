import re
print('学生登录系统\n人工智能3182班')
path = '学生花名册.txt'
name = input("你好，请输入用户名：")
with open(path) as wenjian:
    shuru=wenjian.readlines()
for shus in shuru:
    pi = re.match(shus.rstrip(), name)
    if pi:
        break
if pi == None  :

    print(name+'你并不是本班学生，无法登录！')
else:
    print(pi.group()+'欢迎回来')
