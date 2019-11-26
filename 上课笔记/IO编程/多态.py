'''
ti = []
class Ti(object):
    pass
ti2 = Ti  # 类也可以把它当作数据类型
'''

class Gou(object):
    def __init__(self,name):
        self.name = name
    def xingdong(self):
        print('奔跑')

class Shenggou(Gou):
    def __init__(self,gou):
        super().__init__(gou)
    def xiangdong(self):
        print('飞翔')

class Ren(object):
    def __init__(self,name):
        self.name = name
    def wan(self,dog,dog2):
        print(self.name+'和'+dog.name+'一起玩！')
        dog.xingdong()
        dog2.xingdong()

xiaohei = Gou('小黑')
oudi = Shenggou('欧弟')
buma = Ren('布玛')
xiaohei.xingdong()
buma.wan(xiaohei,oudi)

