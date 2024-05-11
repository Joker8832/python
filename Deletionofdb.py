import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="farih")
cur=conn.cursor()

if conn:
    name=input("Enter The Name Of The Student :")
    cur.execute("DELETE FROM MARK WHERE NAME='%s'"%name)
    print("Deleted Succefully")
    conn.commit()
else:
    print("Name Not Found")
