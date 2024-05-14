import mysql.connector

conn = mysql.connector.connect(host='localhost', user="root", passwd="", database="proj")
cur = conn.cursor()

def add():
    a = int(input("Select An Option (1.Table Menu 2.Update table 3.Exit): "))
    if a == 1:
        def menu():
            b = int(input("Select An Option (1.Insertion 2.Delete a Person Detail 3.Searching 4.Exit): "))
            if b == 1:
                def insertion():
                    rn = int(input("Enter Roll no Of The Student: "))
                    name = input("Enter the person name: ")
                    eng = int(input("Enter The English Mark: "))
                    sl = int(input("Enter The SL Mark: "))
                    math = int(input("Enter The Maths Mark: "))
                    phy = int(input("Enter The Physics Mark: "))
                    chm = int(input("Enter The Chemistry Mark: "))
                    cs = int(input("Enter The CS Mark: "))
                    cur.execute("INSERT INTO student (roll_no, name, Maths, Cs, SL, Physics, Chemistry, English) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (rn, name, math, cs, sl, phy, chm, eng))
                    print("Inserted Successfully")
                    conn.commit()
                    dis = input("Do You Want To Insert More Y/N: ")
                    if dis.upper() == 'Y':
                        insertion()
                    else:
                        menu()

                insertion()

            elif b == 2:
                dn = input("Enter The Name Of The Student: ")
                cur.execute("DELETE FROM student WHERE name = %s", (dn,))
                print("Deleted Successfully")
                conn.commit()
                menu()

            else:
                add()

        menu()

add()
