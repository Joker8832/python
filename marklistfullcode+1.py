import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="proj")
cur=conn.cursor()
if conn:
    def add():
        a=int(input("Select An Option (1.Table Menu 2.Update table 3.Exit)   :"))
        if a==1:
            def min():
                b=int(input("Select An Option (1.Insertion 2.Delete a Person Detail 3.Searching 4.Exit)     :"))
                if b==1:
                    def ins():
                        rn=int(input("Enter Roll no Of The Student  :"))
                        name=(input("Enter the person name  :"))
                        eng=int(input("Enter The English Mark   :"))
                        sl=int(input("Enter The SL Mark :"))
                        math=int(input("Enter The Maths Mark    :"))
                        phy=int(input("Enter The Physics Mark   :"))
                        chm=int(input("Enter The Chemistry Mark :"))
                        cs=int(input("Enter The CS Mark :"))
                        cur.execute("INSERT INTO MARKLIST (roll_no, name, Maths, Cs, SL, Physics, Chemistry, English) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (rn, name, math, cs, sl, phy, chm, eng))
                        print("Inserted Succefully")
                        conn.commit()
                        dis=(input("Do You Want To Insert More Y/N"))
                        if dis=='Y':
                            ins()
                        else:
                            min()
                elif b==2:
                        dn=input("Enter The Name Of The Student :")
                        cur.execute("DELETE FROM MARKLIST WHERE NAME='%s'"%dn)
                        print("Deleted Succefully")
                        conn.commit()
                        min()
                elif b==3:
                    na=input("Enter The Name Of The Student :")
                    cur.execute("SELECT *FROM MARKLIST WHERE NAME='%s'"%na)
                    result=cur.fetchall()
                    for a in result:
                        print("Roll Number :",a[0])
                        print("Name :",a[1])
                        print("Maths Mark:",a[2])
                        print("English Lang Mark:",a[3])
                        print("Cs Mark:",a[4])
                        print("SL Mark:",a[5])
                        print("Physics Mark:",a[6])
                        print("Chemistry Mark:",a[7])
                        print("Total Mark:",a[8])
                        print("Percentage:",a[9])
                        print("Average :",a[10])
                        add()
                else:
                        add()
                
                        ins()
        
            min()
        elif a==2:
                cur.execute("UPDATE MARKLIST SET TOTAL=Maths+Cs+SL+Physics+Chemistry+English")
                print("Total Mark Updated Succefully")
                conn.commit()
                cur.execute("UPDATE MARKLIST SET PERCENTAGE=(TOTAL/360)*100")
                print("Percentage Updated Succefully")
                conn.commit()
                cur.execute("UPDATE MARKLIST SET AVERAGE=TOTAL/6")
                print("Average Updated Succesfully")
                conn.commit()
                print("All Set Sir")
                add()
        else:
             exit()
    add()           
