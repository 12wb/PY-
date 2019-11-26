import pymysql

class chengjiku(object):
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    def connet(self):
        self.db = pymysql.connect(self.host, self.user, self.password, self.dbname)
        self.cursor = self.db.cursor()

    def cloase(self):
        self.cursor.close()
        self.db.close()

def get_one(self, sql):
        res = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print('查询失败')
        return res
def __edit(self, sql):
        count = 0
        try:
            self.connet()
            count = self.curor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print('你的操作有误')
            self.db.rollback()

def insert(self, sql):
        return self.__edit(sql)


def insert(self, sql):
        return self.__edit(sql)
