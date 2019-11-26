import tkinter
import tkinter.font as tkFont 
import socket
import threading
import time
import sys
from tkinter import messagebox

class ServerUI():
    title = '服务器端'
    ip = '127.0.0.1'
    port = 5505
    flag = False

    # 初始化类的相关属性，类似于Java的构造方法
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(self.title)
        
        # 窗口面板,用4个frame面板布局
        self.frame = [tkinter.Frame(),tkinter.Frame(),tkinter.Frame(),tkinter.Frame()]

        # 显示消息Text右边的滚动条
        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

        # 显示消息Text，并绑定上面的滚动条
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.chatText = tkinter.Listbox(self.frame[0],width=70,height=18,font=ft)
        # Listbox列表框,固定的一行
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1,fill=tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview
        self.frame[0].pack(expand=1,fill=tkinter.BOTH)
        '''在显示第一个面板布局，
        expand=1 1可扩展，0不可扩展，fill=tkinter.BOTH
        当GUI窗体大小发生变化时，widget在x，y两方向跟随GUI变化'''

        # 标签，分开消息显示Text和消息输入Text
        label = tkinter.Label(self.frame[1],height=2)
        label.pack(fill=tkinter.BOTH)  # 将标签添加到主窗口
        self.frame[1].pack(expand=1,fill=tkinter.BOTH)
        '''显示第二个面板布局，
        expand=1 1可扩展，0不可扩展，fill=tkinter.BOTH
        当GUI窗体大小发生变化时，widget在x，y两方向跟随GUI变化'''

        # 输入消息Text的滚动条
        self.inputTextScrollBar = tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

        # 输入消息Text，并与滚动条绑定
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.inputText = tkinter.Text(self.frame[2],width=70,height=8,font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1,fill=tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.inputText.yview
        self.frame[2].pack(expand=1,fill=tkinter.BOTH)
        '''在显示第三个面板布局，
               expand=1 1可扩展，0不可扩展，fill=tkinter.BOTH
               当GUI窗体大小发生变化时，widget在x，y两方向跟随GUI变化'''

        # 发送消息按钮
        self.sendButton=tkinter.Button(self.frame[3],text=' 发 送 ',width=10,command=self.sendMessage)
        self.sendButton.pack(expand=1,side=tkinter.BOTTOM and tkinter.RIGHT,padx=25,pady=5)
        '''expand=1 1可扩展，0不可扩展，side=tkinter.BOTH
           边在x，y两方向跟随GUI变化并显示在右边，padx=25与pady=5意思是设置x与y轴的大小'''

        # 关于按钮
        self.closeButton = tkinter.Button(self.frame[3], text=' 点我', width=10, command=self.Command1_Cmd)
        self.closeButton.pack(expand=1, side=tkinter.RIGHT, padx=25, pady=5)

        # 关闭按钮
        self.closeButton=tkinter.Button(self.frame[3],text=' 关 闭 ',width=10,command=self.close)
        self.closeButton.pack(expand=1,side=tkinter.RIGHT,padx=25,pady=5)
        '''expand=1 1可扩展，0不可扩展，side=tkinter.BOTH
                   边在x，y两方向跟随GUI变化并显示在右边，padx=25与pady=5意思是设置x与y轴的大小'''
        self.frame[3].pack(expand=1,fill=tkinter.BOTH)
        '''在显示第四个面板布局，
                       expand=1 1可扩展，0不可扩展，fill=tkinter.BOTH
                       当GUI窗体大小发生变化时，widget在x，y两方向跟随GUI变化'''


    # 显示关于的内容
    def Command1_Cmd(self,event=None):
        messagebox.showinfo(title='关于', message='server' + "\n" + '毕志刚  ' + "\n" + '人工智能3182班')

    # 接收消息
    def receiveMessage(self):
        # 建立Socket连接
        self.serverSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSock.bind((self.ip,self.port))
        self.serverSock.listen(15)
        self.buffer = 1024
        self.chatText.insert(tkinter.END,'服务器已经就绪......')

        # 循环接受客户端的连接请求
        while True:
            self.connection,self.address = self.serverSock.accept()  # 接收客户端的请求
            self.flag = True  # 设置一个变量
            while True:
                # 接收客户端发送的消息
                self.cientMsg = self.connection.recv(self.buffer).decode('utf-8')
                if not self.cientMsg:
                    continue
                elif self.cientMsg == 'Y':
                    self.chatText.insert(tkinter.END,'服务器端已经与客户端建立连接......')
                    self.connection.send('Y'.encode())  # 把消息加密发送给客户端
                elif self.cientMsg == 'N':
                    self.chatText.insert(tkinter.END,'服务器端与客户端建立连接失败......')
                    self.connection.send('N'.encode())
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    self.chatText.insert(tkinter.END, '比尔盖茨 ' + theTime +' ：\n')
                    self.chatText.insert(tkinter.END, '  ' + self.cientMsg)

    # 发送消息
    def sendMessage(self):
        # 得到用户在Text中输入的消息
        message = self.inputText.get('1.0',tkinter.END)  # 1.0代表第一行第0列
        # 格式化当前的时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(tkinter.END,  theTime+ '\n' )
        self.chatText.insert(tkinter.END, '毕志刚' + ":"+ message )
        self.chatText.insert(tkinter.END,'  '+ '\n')
        if self.flag == True:
            # 将消息发送到客户端
            self.connection.send(message.encode())
        else:
            # Socket连接没有建立，提示用户
            self.chatText.insert(tkinter.END,'您还未与客户端建立连接，客户端无法收到您的消息\n')
        # 清空用户在Text中输入的消息
        self.inputText.delete(0.0, "end")
        # self.inputText.delete(0.0,message.__len__()-1.0)


    # 关闭消息窗口并退出
    def close(self):
        sys.exit()

    # 启动线程接收客户端的消息
    def startNewThread(self):  # 启动新的线程来接收客户端的消息
        thread=threading.Thread(target=self.receiveMessage)  # 设置一个线程
        thread.setDaemon(True)  # 设置它为守护线程，
        thread.start()  # 启动线程


def main():
    server = ServerUI()  # 调用类
    server.startNewThread() # 调用  类里面 启动线程接收客户端的消息
    server.root.mainloop() # 刷新显示  类里面 构造函数 的界面

if __name__=='__main__':
    main()

