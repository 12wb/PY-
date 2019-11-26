'''
from email.mime.text import MIMEText  # 调用构建邮件文本
 # from email.mime.multipart import MIMEMultipart  # 构建多个元素
 # from email.mime.image import MIMEImage  # 构建邮件图片

# 构建电子邮件内容
msg_text = MIMEText('你好','plain')

import smtplib
while True:
    srv = smtplib.SMTP('smtp.qq.com',25)  # 连接服务器
    srv.login('1005630541@qq.com','ceiwedfyxtyebdfb')  # 登录
    srv.sendmail('1005630541@qq.com','1638709737@qq.com',
             msg_text.as_string())  # 后一个邮箱为对方qq邮箱
'''

'''
from email.mime.text import MIMEText  # 调用构建邮件文本
from email.header import Header  # 调用Header文件
from_address = '2654158887@qq.com'
from_password =''
to_address = ['2654158887@qq.com','']  # 列表可以进行邮件群发

# 构建邮件
msg = MIMEText('zhenksjad','plain','utf-8')  # 内容
msg['from'] = Header('我','utf-8')  # 发件人 标题
msg['to'] = Header('你','utf-8')  # 收件人 标题
sub = '一次事件'
msg['subject'] = Header(sub,'utf-8')  # 主题

# 发送邮件
try:
    import smtplib
    srv = smtplib.SMTP('smtp.qq.com',25)  # 连接服务器
    srv.login('2654158887@qq.com','euguhnqyfficeaei')  # 登录
    srv.sendmail('2654158887@qq.com','2981267072@qq.com',
                 msg.as_string())  # 后一个邮箱为对方qq邮箱
    srv.quit()
except Exception as e:
    print(e)
'''


from email.mime.text import MIMEText  # 调用构建邮件文本
from email.header import Header  # 调用Header文件
from email.mime.multipart import MIMEMultipart  # 调用多个方式文件
from_address = '2654158887@qq.com'
from_password =''
to_address = ['2654158887@qq.com','']  # 列表可以进行邮件群发

# 构建邮件
htmltext = '''
<p>python 测试</p>
<p><a herf="http://www.baidu.com">欢迎进入百度</a></p>
'''
msg = MIMEMultipart('曾经，意外，他与她相爱，在不会犹豫的时代。')  # 内容
# msg = MIMEText(htmltext,'html','utf-8')  # 内容
msg['from'] = Header('毕志刚','utf-8')  # 发件人 标题
msg['to'] = Header('康老师','utf-8')  # 收件人 标题
sub = 'I am a hacker'
msg['subject'] = Header(sub,'utf-8')  # 主题

# 添加附件
with open('qqq.txt','rb') as file:
    s = file.read()
    m = MIMEText(s,'base64','utf-8')
    m['Content-Type'] = 'application/octet-stream'
    m['Content-Disposition'] = 'attachment,filename=''qqq.txt'
    # 添加到mul对象中
    msg.attach(m)
    print('发送成功')
# 发送邮件
try:
    import smtplib
    srv = smtplib.SMTP('smtp.qq.com',25)  # 连接服务器
    srv.login('2654158887@qq.com','euguhnqyfficeaei')  # 登录
    srv.sendmail('2654158887@qq.com','1005630541@qq.com',
                 msg.as_string())  # 后一个邮箱为对方qq邮箱
    srv.quit()
except Exception as e:
    print(e)








