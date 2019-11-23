"""
   编写一个程序,模拟用户注册,登录的数据库行为

   stu->user表

   * 用户名不能重复
   * 要包含用户名和密码字段
"""

import pymysql
import re
class User:
    def __init__(self,database):
        #连接数据库
        self.db=pymysql.connect(user='root',
                           passwd='123456',
                           database=database,
                           charset='utf8')
        #获取游标
        self.cur=self.db.cursor()
    def zhuce(self,name,mima):
        sql="select * from user where name=%s;"
        self.cur.execute(sql,[name])
        r=self.cur.fetchone()
        if r:
            return False
        sql = "insert into user values(%s,%s);"
        try:
            self.cur.execute(sql, [name,mima])
            self.db.commit()
            return True
        except:
            self.db.rollback()
    def denglu(self,name,mima):
        sql = "select * from user where name=%s and mima=%s;"
        self.cur.execute(sql, [name,mima])
        r = self.cur.fetchone()
        if r:
            return True

if __name__ == '__main__':
    w01=User('dict')
    q=input('输入1注册，输入2登录')
    if q=='1':
        name=input('输入用户名')
        mima=input('密码')
        e=w01.zhuce(name,mima)
        if e:
            print('Ok')
        else:
            print('Flase')
    elif q=='2':
        name = input('输入用户名')
        mima = input('密码')
        y=w01.denglu(name,mima)
        if y:
            print('OK')
        else:
            print('F')

