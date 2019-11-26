'''import  socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",9999))
while True:         #调用了while循环并且是True代表永远不会断开
    a=input()       #调用了input 语句
    client.send(a.encode("utf-8"))
    # 客户端socket 发送数据给服务端
    data = client.recv(1024)
    # 接受的数据
    print(data.decode("utf8"))
import  socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",9999))

server.listen()
sock,addr=server.accept()
while True:        #调用了while循环并且是True代表永远不会断开
    data = sock.recv(1024)
    print(data.decode("utf-8"))
    a=input("")          #调用了input 语句
    sock.send(a.encode("utf-8"))'''

from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('127.0.0.1', 8080)
tcpSerSocket.bind(address)

# 	使⽤socket创建的套接字默认的属性是主动的，使⽤listen将其变为被动的，这样就可以接
tcpSerSocket.listen(5)

while True:
    # 如果有新的客户端来链接服务器，那么就产⽣⼀个信⼼的套接字专⻔为这个客户端服务器
    # #	newSocket⽤来为这个客户端服务
    # #	tcpSerSocket就可以省下来专⻔等待其他新客户端的链接
    newSocket, clientSocket = tcpSerSocket.accept()
    while True:
        # 接收对⽅发送过来的数据，最⼤接收1024个字节
        recvData = newSocket.recv(1024)

        if len(recvData) > 0:
            print("接收数据:\n" + recvData.decode('utf8'))
        else:
            break
        # 发送数据到客户端
        sendData = input("发送数据:\n")
        newSocket.send(sendData.encode('utf8'))
    newSocket.close()
