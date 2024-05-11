import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="farih")
cur=conn.cursor()
tn=input("Enter a table name:")
sub1=(input("Enter the first subjcect name:"))
sub2=(input("Enter the second subject name:"))
if conn:
    cur.execute("CREATE TABLE %s (NAME CHAR(20),%s INT, %s INT)"%(tn,sub1,sub2))
    print("Table Created Successfully")
   
