import tkinter
# 建立一个窗口对象（容器）
win = tkinter.Tk()  # 实例
win.title('我是一个窗口')  # 窗口名称
win.geometry('400x400+600+20')  # 窗口大小

# 控件绑定变量
e = tkinter.Variable()  # 绑定变量
entry = tkinter.Entry(win, textvariable=e,show='*')  # show代表输入的值用*代替
entry.pack()

def gongnenyi():
    print(e.get())
button = tkinter.Button  # 加入一个按钮
button = tkinter.Button(win, text='功能一', width=10, height=10,
                        command=gongnenyi)
button.place(x=100, y=100)

# 拿出变量的值
zhi = e.get()
print(zhi)


win.mainloop()  # mainloop()无限循环, 运行后弹出一个窗口
