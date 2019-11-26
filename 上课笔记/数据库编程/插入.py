import pymysql
# 打开数据库连接，参数一：主机名 参数二：用户名  参数三：密码  参数四：数据库名称
db = pymysql.connect('localhost','root','itcast','test')
# 在db数据连接中创建一个游标，处理数据库操作
cursor = db.cursor()


aaa = '百年孤独'
bbb = '文学'
ccc = '20.11'
ddd = '2019-01-01'

sql ='''
insert into books(name, category, price, publish_time)
value('%s','%s','%s','%s')
'''%(aaa,bbb,ccc,ddd)

"""
sql ='''
insert into books(name, category, price, publish_time)
value('核心编程','教材','99.00','2016-03-03')
'''"""


cursor.execute(sql)

sqll = '''
insert into books(name, category, price, publish_time)
value('核心编程abc',bbb,ccc,ddd)
'''

try:

    cursor.execute(sql)
    # 提交一致性数据
    db.commit()
except:
    print('你错了')
    # 发生错误时滚回
    cursor.execute(sqll)
db.close()

