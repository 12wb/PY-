'''
# 全局变量
num = 100
print(num)
def s():
    global num
    num += 1
s()
print(num)

num = [11,22,33]
print(num)
def n():
    num.append(44)
n()
print(num)
'''

import threading
import time
g_num = 400
def plus():
    time.sleep(2)
    global g_num
    g_num += 50
    print(g_num)
def minus():
    time.sleep(1)
    global g_num
    g_num -= 50
    print(g_num)

print(g_num)
t1 = threading.Thread(target=plus)
t2 = threading.Thread(target=minus)
t1.start()
t2.start()