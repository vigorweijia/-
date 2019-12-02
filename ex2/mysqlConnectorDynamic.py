import mysql.connector
cnn = mysql.connector.connect(user='root', passwd='1234', database='ex2')
cursor = cnn.cursor(prepared=True)

sql = "select * from staff where staff_no=%s"
num = input("请输入查询的员工号：")
cursor.execute(sql, (num,))
for each in cursor:
    print(each)

cursor.close()
cnn.close()
