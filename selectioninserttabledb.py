import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="farih")
cur=conn.cursor()

if conn:
    def add():
        sel=int(input("Select An Option (1.Insert 2.Exit)"))
        if sel==1:
            name=input("Enter The Name Of The Student   :")
            m1=int(input("Enter The Mark Of English  :"))
            m2=int(input("Enter The Mark Of Maths   :"))
            cur.execute("INSERT INTO mark VALUE('%s','%s','%s')"%(name,m1,m2))
            conn.commit()
            print("The Information Inserted Succefully")
            add()
        if sel==2:
            print("Exited")
add()
