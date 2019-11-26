import tkinter
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('用户登录系统')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小

# framel是一个子容器
framel = tkinter.Frame(win, width=100, height=100)
framel.place(x=100, y=100)
# waster=win
button2 = tkinter.Button(win, text='关闭窗口', width=10, height=10,
                        command=win.quit)
button2.place(x=1, y=1)
# master=framel
button1 = tkinter.Button(framel, text='关闭窗口', width=10, height=10,
                        command=win.quit)
button1.place(x=1, y=1)


win.mainloop()  # mainloop()无限循环, 运行后弹出一个窗口
