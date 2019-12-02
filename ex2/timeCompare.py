import time
import mysql.connector
from DBUtils.PooledDB import PooledDB

def useMysqlConnector():
    cnn = mysql.connector.connect(user='root', passwd='1234', database='ex2')
    cursor = cnn.cursor()
    cursor.execute("select * from staff")
    res = cursor.fetchall()
    #for each in res:
    #    print(each)
    cursor.close()
    cnn.close()

def usePooledDB(pool):
    cnn = pool.connection()
    cursor = cnn.cursor()
    cursor.execute("select * from staff")
    res = cursor.fetchall()
    #for each in res:
    #    print(each)
    cursor.close()
    cnn.close()

if __name__=="__main__":
    startTime = time.time()
    for i in range(0,2000):
        useMysqlConnector()
    endTime = time.time()
    print('mysql.connector cost: ' + str(endTime-startTime))

    startTime = time.time()
    pool = PooledDB(mysql.connector, user='root', passwd='1234', database='ex2')
    for i in range(0,2000):
        usePooledDB(pool)
    endTime = time.time()
    print('PooledDB cost: ' + str(endTime - startTime))