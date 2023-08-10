# TABLE TO TABLE COPY
# CTAS: CREATE-TABLE-AS-SELECT

import pymysql

con=pymysql.connect(host='localhost',user='root',password='root',database='mydb01')

# Creating a Cursor Object

cursor=con.cursor()

cursor.execute("create table ignou_student as select * from student_info")

cursor.execute("select * from ignou_student")

for row in cursor:
    print(row)

con.close()
cursor.close()
