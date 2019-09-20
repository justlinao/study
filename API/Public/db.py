import pymysql
import sys
db_host = '10.225.75.101'
db_port = '3306'
db_user = 'banciyuan_boe_w'
db_passwd = 'ZWqa7Nfp1oxBJQT_MtbODjzrpf2QySZP'
db = 'banciyuan_boe'


class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host=db_host,
            port=int(db_port),
            user=db_user,
            passwd=db_passwd,
            db=db,
            charset='utf8'
        )
        print(self.conn)

    def query_db(self, sql):
        '''
        :param sql: 被执行的sql语句
        :return: 返回查询的结果
        '''
        cur = self.conn.cursor()  # 建立游标
        cur.execute(sql)  # sql语句
        self.conn.commit()  # 提交
        result = cur.fetchall()  # 获取所有查询结果
        # for i in result:
        #     print(i[1])
        cur.close()
        self.conn.close()
        for i in result:
            print(i, '\n')
        return result

    def change_db(self, sql):
        # 获取连接
        cur = self.conn.cursor()  # 建立游标
        try:
            cur.execute(sql)  # 执行sql
            self.conn.commit()  # 提交更改
        except Exception as e:
            self.conn.rollback()  # 回滚
        finally:
            cur.close()  # 关闭游标
            self.conn.close()  # 关闭连接

    # 封装数据库常用操作
    def check_user(self, name):
        # 注意sql中''号嵌套的问题
        sql = "select * from user where name = '{}'".format(name)
        result = DB().query_db(sql)
        return True if result else False

    def add_user(self, name, password):
        sql = "insert into user (name, passwd) values ('{}','{}')".format(name, password)
        DB().change_db(sql)

    def del_user(self, name):
        sql = "delete from user where name='{}'".format(name)
        DB().change_db(sql)


if __name__ == '__main__':
    DB().query_db('INSERT INTO `bcy_ad_user_test`(device_id,avg_time,avg_like,interval_day) VALUES(6689405424888232737,1,1,2)')
    #  插入一条注释
