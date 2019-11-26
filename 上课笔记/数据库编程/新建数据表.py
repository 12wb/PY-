import pymysql
# 打开数据库连接，参数一：主机名 参数二：用户名  参数三：密码  参数四：数据库名称
db = pymysql.connect('localhost','root','itcast','test')
# 在db数据连接中创建一个游标，处理数据库操作
cursor = db.cursor()

# cursor.execute('drop table if exists books')
sql = '''
create table books(
id int(8) not null auto_increment,
name varchar(50) not null,
category varchar(50) not null,
price decimal(10,2) default null,
publish_time date default null,
primary key(id)
)engine=MyISAM auto_increment=1 default charset=utf8;
'''
cursor.execute(sql)