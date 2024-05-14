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
                        cur.execute("insert into student (roll_no,name,Maths,Cs,SL,Physics,Chemistry,English) values (%s,'%s',%s,%s,%s,%s,%s,%s)"%(rn,name,math,cs,sl,phy,chm,eng))
                        print("Inserted Succefully")
                        conn.commit()
                        dis=int(input("Do You Want To Insert More Y/N"))
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
                else:
                        add()
                ins()
            min()    
    add()            


        
