'''# 检测CPU
import threading
import multiprocessing

def locp():
    x = 0
    while True:
        x = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=locp)
    t.start()

for i in range(multiprocessing.cpu_count()):
    t1 = threading.Thread(target=locp)
    t1.start()

for i in range(multiprocessing.cpu_count()):
    t2 = threading.Thread(target=locp)
    t2.start()
'''

import queue
import threading
import time

# 生产者类
class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name = name)
        self.data = queue
    def run(self):
        for i in range(5):
            print('生产者%s加入商品%s'%(self.getName(),i))
            self.data.put(i)
            time.sleep(1)
        print('生产者%s完成'%self.getName())

# 消费者类
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name = name)
        self.data = queue
    def run(self):
        for i in range(5):
            val = self.data.get()  # 有产品就取出
        print('消费者%s将数据取出%s'%(self.getName(),i))
        time.sleep(1)
        print('消费者%s完成'%self.getName())

print('主线程')
workqueue = queue.Queue()  # 建立一个仓库，队列
producer = Producer('生产一号',workqueue)  # 实例化生产者线程
consumer = Consumer('生产二号',workqueue)  # 实力化消费者线程
producer.start()
consumer.start()
producer.join()
consumer.join()