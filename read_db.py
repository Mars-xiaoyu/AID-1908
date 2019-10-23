"""
read_db.py
pymysql 读操作演示
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

# 执行对读操作
# sql = "select name,age from class1 where sex='m';"
# name = input("Name:")
# sql = "select * from interest where name='%s';" % name
sql = "select * from class1 where sex=%s and score>%s;"
cur.execute(sql, ['m', 85])  # 执行语句

"""
# 迭代cur获取查询结果
for i in cur:
    print(i)
"""

"""
# 获取一个查询结果
one_row = cur.fetchone()
print(one_row)
"""

"""
# 获取多个查询结果
many_row = cur.fetchmany(2)
print(many_row)
"""

# 获取所有查询结果
all_row = cur.fetchall()
print(all_row)

# 关闭游标和数据库链接
cur.close()
db.close()
