import mysql.connector
from DBUtils.PooledDB import PooledDB

pool = PooledDB(mysql.connector, 5, host='localhost', user='root', passwd='1234', db='ex2', port=3306)
con = pool.connection()
cursor = con.cursor()

cursor.execute('select * from staff')
res = cursor.fetchall()
for each in res:
    print(each)

cursor.close()
con.close()

