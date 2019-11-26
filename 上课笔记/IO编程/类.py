"""
class Ren():
   def __init__(self,name,age): #构造属性 属性-变量    self是传递参数(形参-实参）init内部函数
       self.name=name
       self.age =age
       
   def baoshu(self): #self传递baoshu  方法-功能（函数）    实例 = 变量+类名+实参
       print(self.name+'已经'+str(self.age)+'岁了。')
   xiaofang='小方'
   
   def _del_(self):#析构函数
       print(self.name+'毕业了!')
xiaoming=Ren('小明',6)
xiaohong=Ren('小红',8)
xiaoming.baoshu()
xiaohong.baoshu()

#小红特有属性
xiaohong.xiaofang='小芳'
print(xiaohong.xiaofang)
print(xiaoming.xiaofang)
"""


'''
class R(object ):
    def __init__(self,name):
        self.name = name
    def r(self):
        print('self.name+'is R)

class Ra(R):#继承R
    def __init__(self,name,age):#冒号是属性来源
        self.age = age
        self.name = name
        super().__init__(name)#super是继承的父类 ，只用于单继承 。      单继承只有一个父类
    def r(self):
        print(self.name + 'is' 'r')


class R(object ):
    def __init__(self,name):
        self.name = name
    def r(self):
        print(self.name + 'is' 'R')

class Ra(R):#继承R
    def __init__(self,name,age):#冒号是属性来源
        self.age = age
        self.name = name
        super().__init__(name)#super是继承的父类 ，只用于单继承 。      单继承只有一个父类
    def r(self):
        print(self.name + 'is' 'r')
'''



