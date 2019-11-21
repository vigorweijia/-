import mysql.connector
cnn = mysql.connector.connect(user='root',passwd='1234',database='ex2')
cursor = cnn.cursor()

#查询staff表中的姓名，职工号和年龄
cursor.execute("select staff_name,staff_no,age from staff")
for staff_name, staff_no, age in cursor:
    print(staff_name, staff_no, age)

print('================================')

#查询参与项目'PROJ-A-A'的职工姓名
cursor.execute("select staff_name from staff where staff_no in (select staff_no from job,project where job.project_no=project.project_no and project.project_name = 'PROJ-A-A')")
for staff_no in cursor:
    print(staff_no)

print('================================')

#插入新员工('Jiang', 10013, 36, 140000, 104)
cursor.execute("insert into staff values('Jiang',10013,36,140000,104)")

#将新员工的薪水扣除5000
cursor.execute("update staff set salary=salary-5000 where staff_no=10013")

#查询薪水最高的职工
cursor.execute("select staff_name,salary from staff S1 where not exists(select * from staff where S1.salary < salary)")
for staff_name, salary in cursor:
    print(staff_name, salary)

print('================================')

#删除新员工
cursor.execute("delete from staff where staff_no=10013")

#查询每个部门的最高薪水
cursor.execute("select dept_no,MAX(salary) from staff group by dept_no")
for each in cursor:
    print(each[0], each[1])

print('================================')

#动态SQL
query_string = input("请输入语句：")
cursor.execute(query_string)
for each in cursor:
    print(each)

cursor.close()
cnn.close()
