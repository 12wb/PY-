import pymysql


def main():
    while True:
        # 主菜单
        temp = "数据库模块" \
               "\n1.添加数据表" \
               "\n2.删除数据表" \
               "\n3.修改数据表" \
               "\n4.查询数据表" \
               "\n5.退出数据表"
        print(temp)
        # 用户输入序号
        temp_num = int(input("序号："))

        # 增
        if temp_num == 1:
            add("itcast", "chapter03", "yang")
        # 删
        elif temp_num == 2:
            a1 = input("操作表名：")
            drop("itcast", "chapter03", a1)
        # 改
        elif temp_num == 3:
            a3 = input("原表名：")
            a4 = input("新表名：")
            delete("itcast", "chapter03", a3, a4)
        # 查
        elif temp_num == 4:
            a2 = input("操作表名：")
            select("itcast", "chapter03", a2)
        # 退出
        elif temp_num == 5:
            break
        else:
            print("请输入正确序号")


def add(passwd, sql_name, table_name):
    # 打开数据库连接，参数一：主机名，参数二：用户名，参数名：密码，参数四：数据库名称

    db = pymysql.connect("localhost", "root", passwd, sql_name)

    cursor = db.cursor()

    sql = '''
    create table books(id int(8) not null auto_increment,
    name varchar(50) not null,
    category varchar(50) not null,
    price decimal(10, 2) default null,
    publish_time date default null,
    primary key(id)
    )engine = MyISAM auto_increment = 1 default charset = utf8'''
    sql = sql.replace("books", table_name)
    cursor.execute(sql)
    cursor.close()


def drop(passwd, sql_name, table_name):
    # 打开数据库连接，参数一：主机名，参数二：用户名，参数名：密码，参数四：数据库名称

    db = pymysql.connect("localhost", "root", passwd, sql_name)

    cursor = db.cursor()

    cursor.execute("drop table if exists " + table_name)


def delete(passwd, sql_name, table_name1, table_name2):
    db = pymysql.connect("localhost", "root", passwd, sql_name)
    cursor = db.cursor()

    sql = "alter table 毕志刚 rename LLL;"
    sql = sql.replace("毕志刚", table_name1)
    sql = sql.replace("WWW", table_name2)
    cursor.execute(sql)
    cursor.close()


def select(passwd, sql_name, table_name):
    # db = pymysql.connect("localhost", "root", passwd, sql_name)
    # cursor = db.cursor()
    #
    # sql = """
    # select * from books;
    # """
    # sql.replace("books", table_name)
    #
    # try:
    #     cursor.execute(sql)
    #     result = cursor.fetchmany()
    #     for i in result:
    #         id = i[0]
    #         name = i[1]
    #         category = i[2]
    #         price = i[3]
    #         publish_time = i[4]
    #     print(id, name, category, price, publish_time)
    # except:
    #     print("出错")
    #
    # cursor.close()
    db = pymysql.connect("localhost", "root", passwd, sql_name)

    cursor = db.cursor()
    sql = """
        desc books;
        """
    sql = sql.replace("books", table_name)
    try:

        cursor.execute(sql)
        cursor.close()
        while True:
            result = cursor.fetchmany()
            print(result)
            if result == ():
                break

    except:
        print("出错")


if __name__ == "__main__":
    main()
