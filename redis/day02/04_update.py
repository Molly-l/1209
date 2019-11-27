import redis
import pymysql

class Update:
    def __init__(self):
        self.r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
        self.db=pymysql.connect('localhost','root','123456','userdb',charset='utf8')
        self.cursor=self.db.cursor()
    def update_mysql(self):
        upd='update user set score=%s where name=%s'
        try:
            self.cursor.execute(upd,[score,username])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.r.expire()

    def run(self):
        username=input('')
        score=float
        self.update_mysql(score,username)
        self.update_redis(username,score)