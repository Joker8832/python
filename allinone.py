import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="proj")
cur=conn.cursor()
if conn:
    print("You Are Succefully Entered Into Marklist Table")
    conn.collation()
    def add():
        a=int(input("Select An Option (1.Table Menu 2.Exit)   :"))
        if a==1:
            opt=int(input("Selection An Option (1.Insert 2.Delete 3.Search )"))
            if opt==1:
                rollno=int(input("Enter The Roll Number :"))
                name=input("Enter The Name :")
                eng=int(input("Enter The English Mark   :"))
                sl=int(input("Enter The SL Mark   :"))
                phy=int(input("Enter The Physics Mark   :"))
                chem=int(input("Enter The Chemistry Mark   :"))
                cs=int(input("Enter The Cs Mark   :"))
                math=int(input("Enter The Maths Mark   :"))
                cur.execute("INSERT INTO MARKLIST VALUE ('%s','%s','%s','%s','%s','%s','%s','%s','','','')"%(rollno,name,eng,sl,phy,chem,cs,math))
                print("Table Created Succesfully")                
                conn.commit()
                add()
            elif opt==2:
                name=input("Enter The Name Of The Student :")
                cur.execute("DELETE FROM MARKLIST WHERE NAME='%s'"%name)
                print("Deleted Succefully")
                conn.commit()
                add()
            elif opt==3:
                    name=input("Enter The Name Of The Student :")
                    cur.execute("SELECT *FROM MARKLIST WHERE NAME='%s'"%name)
                    result=cur.fetchall()
                    for a in result:
                        print("Roll Number :",a[0])
                        print("Name :",a[1])
                        print("English Mark:",a[2])
                        print("Second Lang Mark:",a[3])
                        print("Physcis Mark:",a[4])
                        print("Chemistry Mark:",a[5])
                        print("Computer Science Mark:",a[6])
                        print("Maths Mark:",a[7])
                        add()                       

        elif a==2:
             exit()
        else:
             print("Invalid Option")
             add()
add()
