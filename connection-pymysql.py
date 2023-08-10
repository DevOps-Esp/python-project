# Creating a database within the mysql

import pymysql

# Creating Connection object
con=pymysql.connect(host="localhost",user='root',password='root')
# here con is the connection object
print('Connection established sucessfully')

# Creating cursor object
cur=con.cursor() # here cur1 is the cursor object

# Within the cursor object (curl) we have execute() method, using which we can
# write any valid sql query

cur.execute("create database mydb01")
print("DATABASE CREATED SUCESSFULLY !!")

cur.close()

con.close()
