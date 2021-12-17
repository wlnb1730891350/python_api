"""
============================
Author:向飞
Time:2020/12/25 19:50
E-mail:947985203@qq.com
============================
"""
import pymysql
from commons.handle_config import conf

class HandleDB():

    def __init__(self,host,port,user,password,*args,**kwargs):
        self.conn=pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset='utf8',
            # cursorclass=pymysql.cursors.DictCursor  # 设置游标对象返回数据类型（字典）默认元组
            *args, **kwargs
        )

    def find_all(self,sql):
        '''返回所有数据'''
        with self.conn as cur:
            cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        return res

        # 0.9.3之后的pymysql
        # cur = self.conn.cursor()
        # cur.execute(sql)
        # res = cur.fetchall()
        # cur.close()
        # return res

    def find_one(self,sql):
        '''返回一条数据'''
        with self.conn as cur:
            cur.execute(sql)
        res=cur.fetchone()
        cur.close()
        return res

    def find_count(self,sql):
        '''返回查询数据条数'''
        with self.conn as cur:
            res=cur.execute(sql)
        cur.close()
        return res

    # def __del__(self):
    #     self.conn.close()

db=HandleDB(host=conf.get('mysql','host'),
            port=conf.getint('mysql','port'),
            user=conf.get('mysql','username'),
            password=conf.get('mysql','password')
            )
# 不同数据库实例化不同的对象
db2=HandleDB(host=conf.get('mysql_1','host'),
            port=conf.getint('mysql_1','port'),
            user=conf.get('mysql_1','username'),
            password=conf.get('mysql_1','password')
            )

if __name__ == '__main__':
    sql='SELECT mobile_phone FROM futureloan.member where mobile_phone="15074480684"'
    res=db.find_count(sql)
    print(res,type(res))


