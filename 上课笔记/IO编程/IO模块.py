'''
# 查看模块的函数
import io
s = dir(io)
for si in s:
    print(si)
'''
from io import StringIO # StringIO给我们在内存内部进行运行的可能
file = StringIO()  # 定义一个功能
file.write('读取')
file.write('内存')
file.write('数据')
# fr = file.read()
# print(fr)
print(file.getvalue())

'''
with open('files','w') as files:
    files.write('读取')
    files.write('内存')
    files.write('数据')
with open('files','r') as files:
    frs = files.read()
    print(frs)
'''

from io import BytesIO
data = ('春眠不觉晓，处处闻啼鸟，夜来风雨声，花落知多少。utf_8')  # 定义一个变量
fileB = BytesIO(data)
print(fileB.read())