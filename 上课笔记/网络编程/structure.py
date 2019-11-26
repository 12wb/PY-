import smtplib
from email.mime.multipart import MIMEMultipart  # 构建多个元素
from email.mime.image import MIMEImage  # 构建邮件图片
from email.mime.text import MIMEText  # 调用构建邮件文本
from email.header import Header  # 调用Header文件
# 构建基础邮件
send = '2654158887@qq.com'
password = 'euguhnqyfficeaei'
recv = ['2654158887@qq.com']
# mixed--混合型
# alternative--文本混合
# related--多媒体元素
msgRoot = MIMEMultipart('mixed')

# 邮件头
msgRoot['From'] = Header('你朋友的邮箱@qq.com','utf-8')  # 你的朋友
msgRoot['To'] = Header('测试人员','utf-8')
msgRoot['Subject'] = Header('I am a hacker','utf-8')  # 主题

# 普通文本
text_text = '这个就是测试的普通文本。'
msg_text = MIMEText(text_text,'plain','utf-8')

# 超文本(超链接)
mail_msg = '''
<p>Python邮件发送超文本测试^^^</p>
<p><a herf = "http://www.baidu.com">百度搜索链接</a><p>
<p>添加的图片：</p>
<p><img src = "cid:image1"></p>
'''
msg_html = MIMEText(mail_msg,'html','utf-8')

# 指定图片为当前目录
with open('test.jpg','rb') as file:
    msg_Image = MIMEImage(file.read())
    msg_Image.add_header('Content-ID','<image1>')

# 构造附件
with open('1111.txt','rb') as sendfile:
    msg_att = MIMEText(sendfile.read(),'base64','utf-8')
    msg_att['Content-Type'] = 'application/octet-stream'
    msg_att.add_header('Content-Disposition','attachment',filename='abc.txt')

msgRoot.attach(msg_text)
msgRoot.attach(msg_html)
msgRoot.attach(msg_Image)
msgRoot.attach(msg_att)

try:
    s = smtplib.SMTP('smtp.qq.com',25)
    s.login(send,password)
    s.sendmail(send,recv,msgRoot.as_string())
except:
    print('出错')