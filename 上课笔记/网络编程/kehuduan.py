# 爬取学校网址
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接
s.connect(('www.hnu.edu.cn',80))
s.send(b'GET / HTTP/1.1\r\nHOST:www.hnu.edu.cn\r\nConnection:close\r\n\r\n')  # 建立连接

# 接收数据
data = []
while True:
    d = s.recv(1024)  # 按字节接收数据
    if d:
        data.append(d)  # 将接收的数据加入列表
    else:
        break

datab = b''.join(data)  # 转换成二进制
s.close()
print(datab)

header, html = datab.split(b'\r\n\r\n',1)
print(header.decode("utf-8"))
# 创建文件
with open("wodewangzhi.html","wb") as file:
    file.write(html)