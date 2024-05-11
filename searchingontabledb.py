import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="farih")
cur=conn.cursor()

if conn:
    name=input("Enter The Name Of The Student :")
    cur.execute("SELECT *FROM MARK WHERE NAME='%s'"%name)
    result=cur.fetchall()
    for a in result:
        print("Name :",a[0])
        print("English Mark :",a[1])
        print("Maths Mark :",a[2])
        
else:
    print("Name Not Found")
