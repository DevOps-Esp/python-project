import pymysql as c
con=c.connect(host="localhost",database='python_db',user="root", passwd='root')
if con.is_connected():
    print("Sucessfully Connected...")
    
