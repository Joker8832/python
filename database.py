import mysql.connector

conn=mysql.connector.connect(host='localhost',user="root", passwd="")
cur=conn.cursor()
name=input("Enter A Name :")
if conn:
    cur.execute("CREATE DATABASE %s" %name)
    print(name," Created Successfully")