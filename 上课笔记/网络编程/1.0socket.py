import socket
#服务端
s = socket.socket() #创建连接
#s.close()
s.bind(('127.0.0.1',8080))#绑定地址
s.listen(5) #监听

while True:
    c,addr = s.accept()#建立连接
    data = c.recv(1024)#接收数据,参数为多少字节
    print(data)
    str = '欢迎登陆人工智能3182班主页'.encode(encoding='gb2312')
    c.sendall(b'HTTP/1.1 200 OK\r\n\r\n ')
    c.close() #发送数据

