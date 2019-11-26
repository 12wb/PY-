import threading
import time
num = 0
mutex = threading.Lock()  # 将锁实例化,创建锁

def s1(chuandi):
    global num
    mutex.acquire()  # 给全局变量num上锁
    for i in range(chuandi):
        num += 1
    print('线程一的计算结果：%d'%num)
    mutex.release()  # 释放锁

def s2(chuandi):
    global num
    mutex.acquire()
    for i in range(chuandi):
        num += 1
    print('线程二的计算结果：%d'%num)
    mutex.release()
def main():
# args传递参数给线程方法，且值必须为元组形式
    t1 = threading.Thread(target=s1,args=(1000000,))
    t2 = threading.Thread(target=s2,args=(1000000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(1)
    print('最后的计算结果：%d'%num)

if __name__ == '__main__':
    main()