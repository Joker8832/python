import mysql.connector
conn=mysql.connector.connect(host='localhost',user="root", passwd="", database="proj")
cur=conn.cursor()
if conn:
    def add():
        a=int(input("Select An Option (1.Database Menu 2.Table Menu 3.Exit)   :"))
        if a==1:
            b=int(input("Select An Option (1.Create A Colum 2.Delete a column 3.Updation of column 4.Return)     :"))
            if b==1:
                def dis():
                     tna=input("Enter the Column name  :")
                     tnu=int(input("Enter the type of data (1.int 2.char)    :"))
                     if tnu==1:
                        ac=("int")
                     elif tnu==2:
                          ac=("char")
                     else:
                          print("Your data type in invalid")
                          y=int(input("Are You Confirm To Create (1.Yes/2.No)    :"))
                          if y==1:
                            cur.execute("ALTER TABLE MARKLIST  ADD %s %s"%(tna,tnu))
                            conn.commit()
                            print("Table Created Succesfully")
                          elif y==2:
                              add()
                              tndis=int(input("Do You Want Create More   (1.Yes 2.No)    :"))
                              if tndis==1:
                                  dis()
                              else:
                                  add()
                dis()
add()
