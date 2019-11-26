'''
# 查看模块功能
import os
s = dir(os)
for sl in s:
    print(sl)
'''

'''
# 查看操作系统
import os
print(os.name)
print(os.path)
'''

from  datetime import datetime
import os

bianliang = os.path.abspath('.')
print('          Size     Last  time          Name')
print('-'*50)

for file in os.listdir(bianliang):
    fsize = os.path.getsize(file)
    ftime = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%y-%m-%I-%r')
    flag = '/'if os.path.isdir(file) else''
    print('%10d  %s  %s%s' %(fsize,ftime,file,flag))
