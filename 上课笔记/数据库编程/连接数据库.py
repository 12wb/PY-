import pymysql
# 打开数据库连接，参数一：主机名 参数二：用户名  参数三：密码  参数四：数据库名称
db = pymysql.connect('localhost','root','itcast','test')
# 在db数据连接中创建一个游标，处理数据库操作
cursor = db.cursor()
# 游标方法运行查询语句
cursor.execute('select version();')  # 查询版本
data = cursor.fetchone()
print(data)
# 关闭数据库连接
db.close()