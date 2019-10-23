"""
mysql.py
pymysql 操作数据库流程演示
"""
import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 生成游标对象(操作数据库,执行spl语句)
cur = db.cursor()
# 执行各种对数据库的读写操作

# 关闭游标和数据库链接
cur.close()
db.close()
