import threading
import time
# 单线程模式，串行模式
def video():
    for i in range(5):
        print('放画面'+str(i))
        time.sleep(1)

def sound():
    for i in range(10):
        print('出声音'+str(i))
        print(threading.enumerate())  # 运行结果显示线程
        time.sleep(1)

# 创建一个线程，完成看视频的工作
t1 = threading.Thread(target=video)
# 创建一个线程，完成出声音的工作
t2 = threading.Thread(target=sound)
t1.start()
t2.start()
'''
t1.join()  # t1线程完毕后才能关闭主线程
t2.join()  # t2线程完毕后才能关闭主线程
'''
print(threading.enumerate())
