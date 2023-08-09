#   PYTHON DATABASE CONNECTION (PDBC)
#----------------------------------------------------------------------------

- To connect Python with any database, we require a module.
# What is Module : Module is a file that contains code to perform a specific task
- There are 2 type of modules in python, Built-in or Internal and External module

# Internal modules : Modules which are part of python software/package
Which comes with python package and no need to install are called internal module

# External modules : Modules which are not part of python software/package
To use these external modules we need to download and install them

- Following are the commnly used database and related modules

- 1) Python to connect with mysql -----> we require -----> Pymysql
- 2) Python to connect with Oracle ----> we require -----> cx_Oracle
- 3) Python to connect with sqlserver --> we require --> phodhc

# 1) Downloading and Installing pymysql:
pymysql is an external module & external modules are those which are not part
of python software by using a component called pip

- pip: pip is a package manager which quickly downlaods and install any python
package which is not a part of python software.

pip is available within the installation folder of python i.e.

C:\Program Files\Python311\Scripts\pip

# Installing pymysql module:
C:\Users>pip install pymysql

Python to connect with database and to perform database opertions and to perform
sql queries, we require 2 objects
1. Connection object &
2. Cursor object

# 1. Connection object:
If we call connect() function by providing the connecting parameters then a
connection object is created
The following are the connection parameters
1. Host Name ------> localhost or remotehost (provide the ip address)
2. User name of mysql --------> root
3. password of mysql  -------> root
4. Database name   --------> (data base name)

# CONNECTING PROCESS:
STEP - 1 ======> import pymysql
STEP - 2 ======> (creating connection object)
con=pymysql.connect(host='localhost',user='root',password='root')
here con is the connection object

# 2. creating cursor object
on the connection object, if we pass cursor() method then curser object is created

cur1=con.cursor() # here cur1 is the cursor object

