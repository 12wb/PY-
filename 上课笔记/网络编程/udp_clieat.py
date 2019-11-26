import socket
# 创建UDP的套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = input('请输入：')
try:# 发送请求
    s.sendto(data.encode(),('127.0.0.1',9999))
    print(s.recv(1024).decode())
except:
    s.close()
