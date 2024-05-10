import mysql.connector

conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="asdf")
cur=conn.cursor()
if conn:
    cur.execute("CREATE TABLE MARK (NAME CHAR(20),ENG INT, MATH INT)")
    print("Table Created Successfully")
   