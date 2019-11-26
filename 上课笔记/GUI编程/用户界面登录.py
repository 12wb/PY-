import tkinter
import tkinter.messagebox


def gongnengyi():
    # 控件绑定变量

    p1 = entry1.get()
    p2 = entry2.get()
    if p1 == "" and p2 == "":
        message = "用户名密码不为空"
    elif p1 == "bzg" and p2 == "123":
        message = "登陆成功"
    else:
        message = "用户名与密码不匹配"
    tkinter.messagebox.showinfo(message=message)


# 建立一个窗口对象（容器）
win = tkinter.Tk()
# 窗口名称
win.title("毕志刚")
# 窗口大小
win.geometry("600x600+600+20")

# 创建标签控件
label = tkinter.Label(win, text="用户登录系统", bg="white", fg="black", width=16, height=4, justify="left")
label.pack()
label2 = tkinter.Label(win, text="账号")
label2.place(x=190, y=80)
label3 = tkinter.Label(win, text="密码")
label3.place(x=190, y=120)

# 创建输入框
e = tkinter.Variable()
y = tkinter.Variable()
# 输入框
entry1 = tkinter.Entry(win, textvariable=e)
entry1.place(x=225, y=80)
entry2 = tkinter.Entry(win, textvariable=y, show="*")
entry2.place(x=225, y=120)

# 创建按钮
button1 = tkinter.Button(win, text="登陆", width=8, height=2, command=gongnengyi)
button1.place(x=200, y=200)
button2 = tkinter.Button(win, text="退出", width=8, height=2, command=win.quit)
button2.place(x=350, y=200)


win.mainloop()  # 无限循环，手动窗口关闭即代码停止运行

