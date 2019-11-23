import mysql.connector
from DBUtils.PooledDB import PooledDB
import time
from threading import Thread


class ConnectBase:
    def __init__(self):
        self.pool = self.create_pool()

    def create_pool(self):
        pool = PooledDB(mysql.connector, maxconnections=8, user='root', passwd='1234', database='ex2')
        return pool

    def fun(self, threadCount, iterationTimes):
        for i in range(0, int(iterationTimes/threadCount)):
            cnn = self.pool.connection()
            cursor = cnn.cursor()
            cursor.execute("select * from staff")
            res = cursor.fetchall()
            cursor.close()
            cnn.close()


if __name__ == "__main__":
    threadCount = 4
    iterationTimes = 2000
    connectBase = ConnectBase()
    t1 = Thread(target=connectBase.fun, args=(threadCount, iterationTimes))
    t2 = Thread(target=connectBase.fun, args=(threadCount, iterationTimes))
    t3 = Thread(target=connectBase.fun, args=(threadCount, iterationTimes))
    t4 = Thread(target=connectBase.fun, args=(threadCount, iterationTimes))
    startTime = time.time()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    endTime = time.time()
    print("thread cost time: " + str(endTime - startTime))
