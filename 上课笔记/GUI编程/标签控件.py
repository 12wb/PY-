import tkinter
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('我是一个窗口')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小
# label标签控件
# text文本， bg 背景色， fg 字体颜色
label = tkinter.Label(win, text='我是一个控件', bg='red', fg='black',
                      width=10, height=4, justify='left')
label.place(x=200, y=100)  # 布局显示



win.mainloop()  # mainloop()无限循环, 运行后弹出一个窗口
