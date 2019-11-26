import tkinter
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('我是一个窗口')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小


label1 = tkinter.Label(win, text='我是一个控件', bg='red', fg='green')
label2 = tkinter.Label(win, text='我是一个控件', bg='yellow', fg='black')
label3 = tkinter.Label(win, text='我是一个控件', bg='blue', fg='white')
label1.pack()
label2.pack(side='left')
label3.place(x=100,y=100)


win.mainloop()


import tkinter
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('我是一个窗口')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小


label1 = tkinter.Label(win, text='我是一个控件', bg='red', fg='green')
label2 = tkinter.Label(win, text='我是一个控件', bg='yellow', fg='black')
label3 = tkinter.Label(win, text='我是一个控件', bg='blue', fg='white')
label1.grid(row=1,column=1)
label2.grid(row=2,column=2)
label3.grid(row=3,column=3)


win.mainloop()