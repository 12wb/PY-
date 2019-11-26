import socket
# 创建UDP的套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP创建后数据不返回
# 参数为ip和port的元组
s.bind(('127.0.0.1',9999))
data,address = s.recvfrom(1024)  # 接收请求
# 功能
data = float(data)*1.8+32
send_data = '温度：'+str(data)

print('来自于%s：%s' % address)
s.sendto(send_data.encode(),address)
s.close()