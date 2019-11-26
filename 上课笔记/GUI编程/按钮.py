import tkinter
import tkinter.messagebox # 弹窗模块
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('我是一个窗口')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小

def gongnengyi():
    print('打开一个文件')

# 创建一个按钮控件
# command来绑定方法， 称之为事件
# command指定函数名， 不要括号， 这是一个易错点
button = tkinter.Button(win, text='功能一', width=10, height=10,
                        command=gongnengyi)
button.place(x=100, y=100)
# command可以用内置函数
button2 = tkinter.Button(win, text='关闭窗口', width=10, height=10,
                        command=win.quit)
button2.place(x=100, y=200)



# command可以使用匿名函数
button3 = tkinter.Button(win, text='匿名函数', width=10, height=10,
                        command=lambda:b3(12345678))  # 也可以在lambda后面加print打印结果
button3.place(x=200, y=100)

def b3(yk):
    print(str(yk))

# command调用弹窗
def funct():
    tkinter.messagebox.askyesnocancel(title='这是一个广告',
                                      message='你中计了')


button4 = tkinter.Button(win, text='广告弹窗', width=10, height=10,
                        command=funct)
button4.place(x=200, y=200)


win.mainloop() # mainloop()无限循环, 运行后弹出一个窗口
