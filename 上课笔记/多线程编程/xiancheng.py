import threading
# 继承方式创建线程的类， 再改写，添加方法
class ra(threading.Thread):
    def __init__(self,name,data):
        threading.Thread.__init__(self)
        self.name = name
        self.data = data

    # run方法是唯一要调用的方法，也是最重要的方法
    def run(self):
        print(self.name+'sing'+self.data)
    # 更多的方法必须由run()函数二次调用才能被写进创建的线程
        self.login()
        self.riger()

    def login(self):
        print('dengru')

    def riger(self):
        print('zhuci')


def main():
    t1 = ra('liuhuan', 'song')
    t2 = ra('qiqing', 'songs')
    print(threading.enumerate())
    ''' t1.start()
    t1.join()
    t2.start()
    t2.join()'''
    t1.run()
    print(threading.enumerate())
    t1.start()
    print(threading.enumerate())
    t1.login()
    print(threading.enumerate())
    t1.riger()
    print(threading.enumerate())


    t2.run()

    # start()方法是唯一调用线程的方法，也是最重要的方法
    t2.start()



if __name__ == '__main__': # 读取私有文件
    main()
