import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="farih")
cur=conn.cursor()

if conn:
    name=input("Enter The Name Of The Student   :")
    m1=int(input("Enter The Mark Of English  :"))
    m2=int(input("Enter The Mark Of Maths   :"))
    cur.execute("INSERT INTO mark VALUE('%s','%s','%s')"%(name,m1,m2))
    conn.commit()
    print("The Information Inserted Succefully")
