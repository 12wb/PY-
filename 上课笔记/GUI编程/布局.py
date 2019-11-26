import tkinter
class zilei(tkinter.Tk):
    def __init__(self,name,size,name2):
        tkinter.Tk.__init__(self)
        self.title(name)
        self.geometry(size)
        # 类中定义了一个按钮
        self.button=tkinter.Button(self,text=name2,command=self.fune)
        self.button.place(x=80,y=20)
    # 定义了方法
    def fune(self):
        print('hahahahahahaha')

class Kongjian():
    def __init__(self,master,name,funct,x,y):
        self.name=name
        self.master=master
        self.funct=funct
        self.x=x
        self.y=y
        button=tkinter.Button(self.master,text=self.name,
                              command=self.funct)
        button.place(x=self.x,y=self.y)
win=zilei('这是一个窗口','400x400+600+20','按钮一号')
disl=Kongjian(win,'aaa',win.quit,20,40)
disl2=Kongjian(win,'bbb',win.quit,40,80)

win.mainloop()





