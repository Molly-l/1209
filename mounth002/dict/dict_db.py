import pymysql
class User:
    def __init__(self,database):
        self.db = pymysql.connect(user='root',
                                  passwd='123456',
                                  database=database,
                                  charset='utf8')
        # 获取游标
        self.cur = self.db.cursor()
    def login(self,name,password):
        sql = "select * from user where name=%s and mima=%s;"
        self.cur.execute(sql, [name,password])
        one_row = self.cur.fetchone()
        if one_row:
            return True
        return False

    def register(self,name,password):
        sql = "select * from user where name=%s;"
        self.cur.execute(sql,[name])
        one_row = self.cur.fetchone()
        if one_row:
            print('s')
            return False
        sql="insert into user values (%s,%s);"
        try:
            self.cur.execute(sql,[name,password])
            print('z')
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False
    def query(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        one_row = self.cur.fetchone()
        if one_row:
            return one_row
        return False
    def history(self,name):
        sql="select name,word,time from hist where name=%s;"
        self.cur.execute(sql,[name])
        hist_top10=self.cur.fetchmany(10)
        if hist_top10:
            return hist_top10
        return False
    def insert_history(self,name,word):
        sql="insert into hist (name,word) values(%s,%s);"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
