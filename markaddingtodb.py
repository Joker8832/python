import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="farih")
cur=conn.cursor()

if conn:
    name=input("Enter The Name Of The Student :")
    math=input("Enter The New Mark Of The Maths :")
    cur.execute("UPDATE MARK SET MATH='%s' WHERE NAME='%s'"%(math,name))
    conn.commit()
    print("Updated Successfully") 
else:
    print("Name Not Found")
