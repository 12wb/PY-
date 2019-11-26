import poplib  # 导入方法
# 登录服务器
srv = poplib.POP3_SSL('pop.qq.com')
sender = '2654158887@qq.com'
password = 'euguhnqyfficeaei'
srv.user(sender)
srv.pass_(password)
# stat()方法返回一个元组，为邮件数量和占用空间
msgs,counts = srv.stat()
print('message:{0},size:{1}'.format(msgs,counts))
# 返回所有邮件的编号列表
rsp1,mails1,cotect1 = srv.list()
print(mails1)

# 获取信件
rsp,lines,octets = srv.retr(len(mails1))
# 获得邮件的整个原始文本
msg_count = b'\r\n'.join(lines).decode('utf-8')
# 解析模块
from email.parser import Parser  # 邮件解码模块
from email.header import decode_header  # header文件解码模块
from email.utils import parseaddr
msg = Parser().parsestr(msg_count)  # 解码邮件整体

# str解码
def decondeStr(s):
    value,charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
        return value


# 判断编码
def guessCharset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_tpye = msg.get('Content-Type','').lower()  # 找到内容，转换为小写
        pos = content_tpye.find('charset')
        if pos > 0:
            charset = content_tpye[pos+8:].strip()  # 如果charset包含，则内容为charset为多少
    return charset

# 定义邮件解码方法
def parseMsg(msg,indent = 0):
# 提取头部信息，内容只有一个
    if indent == 0:
        for header in ['From','To','Subject']:
            value = msg.get(header,'')
            if value:
                if header == 'Subject':
                    value = decode_header(value)
                else:
                    hdr,addr = parseaddr(value)
                    name = decondeStr(hdr)
                    value = '{0},{1}'.format(name,addr)
            print('{0},{1},{2}'.format(indent,header,value))

# 提取邮件元素
    if(msg.is_multipart()):
        # 如果邮件为multipart类型，则调用递归解析
        #分包
        parts = msg.get_payload()
        for n,part in enumerate(parts):
            print('{0}spart:{1}'.format(''*indent,n))
            parseMsg(part,indent+1)

    else:  # 最基本的邮件
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content =msg.get_payload(decode=True)
            charset = guessCharset(msg)
            if charset:
                content = content.decode(charset)
            print('{0}Text:{1}'.format(indent,content_type))
        else:
