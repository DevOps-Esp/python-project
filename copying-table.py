import pymysql
# Creating connection object
con=pymysql.connect(host='localhost',user='root',password='root',database='mydb01')
print('Connestion Established Sucessfully')

# Creating cursor object
cursor=con.cursor()

# Execute method within cursor to write sql queries

#1) To create table from another table (Coping table)
'''
cursor.execute("create table student_info_ignou like student_info")
print('Table Created Sucessfully')
'''
#2) To insert data in tables
cursor.execute(" insert into student_info_ignou values (1001,'Ram Charan Singh','B.Tech(Information Technology)','2020-2024','Raipur','9988776655','rcsingh@gmail.com')")
print('Data insterted sucessfully')
cursor.close()
con.commit()
con.close()



