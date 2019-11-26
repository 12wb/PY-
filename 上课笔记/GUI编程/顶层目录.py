import tkinter
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('我是一个窗口')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小

# 创建一个菜单条
menubar = tkinter.Menu(win)
# 关闭窗口，不用布局
win.config(menu = menubar)

# 创建一个菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)
menu1.add_command(label='python',command=lambda:print('运行pycharm'))
menu1.add_separator()
menu1.add_cascade(label='C')
menu1.add_cascade(label='B')
menu1.add_cascade(label='rudy')
menu1.add_cascade(label='object-c')

menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_cascade(label='接口设置')
menu2.add_cascade(label='外观设置')
menu2.add_cascade(label='语言设置')
menubar.add_cascade(label='语言',menu=menu1)
menubar.add_cascade(label='设置',menu=menu2)

win.mainloop()  # mainloop()无限循环, 运行后弹出一个窗口
