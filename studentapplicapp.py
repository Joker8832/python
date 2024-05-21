import mysql.connector
from tkinter import*
import tkinter.messagebox as message 

conn=mysql.connector.connect(host="localhost", user="root", passwd="", database="school")
cur=conn.cursor()
def save():
    name=ent1.get()
    address=ent2.get()
    phone=ent3.get()
    if name=="" or address=="" or phone=="":
        message.askyesnocancel("Inser Data","Please fill all textboxes")
    cur.execute("INSERT INTO student VALUE('%s','%s','%s');"%(name,address,phone))
    conn.commit()
    message.showinfo("Saved Data","Data Saved Success")
def delete():
    name=ent1.get()
    if name=="":
        message.showerror("Error","Name Box Is Not Filled")
    cur.execute("DELETE FROM student WHERE NAME='%s'"%name)
    conn.commit()
    message.showinfo("Deleted","Deleted Succesfully")
def search():
    name=ent1.get()
    if name=="":
        message.showerror("Error","Name Box Not Filled")
    cur.execute("SELECT *FROM student WHERE NAME='%s'"%name)
    result=cur.fetchall()
    for a in result:
        ent1.delete(0,END)
        ent1.insert(0,a[0])
        ent2.insert(0,a[1])
        ent3.insert(0,a[2])
    cur.close()
def edit():
    name=ent1.get()
    if name=="":
        message.showerror("Error","Name Box Is Empty")
    else:
        message.showinfo("Enter","Edited Succesfully")
        address=ent2.get()
        ph=ent3.get()
        conn.commit()
        cur.execute("update student set address='%s',phone='%s' where name='%s'"%(address,ph,name))
        conn.commit()
window=Tk()


window.title("Application Form")
window.geometry("450x300")
window.resizable(False,False)
window.configure(background="white")
window.iconbitmap("favicon.ico")

lbl1=Label(text="Name",foreground="black",bg="white",font="Bold")
lbl1.place(x=40,y=20)
lbl1=Label(text="Address",foreground="black",bg="white",font="Bold")
lbl1.place(x=40,y=60)
lbl1=Label(text="Phone",foreground="black",bg="white",font="Bold")
lbl1.place(x=40,y=100)

ent1=Entry(fg="white",background="blue",font="bold")
ent1.place(x=130,y=20)
ent2=Entry(fg="white",background="blue",font="bold")
ent2.place(x=130,y=60)
ent3=Entry(fg="white",background="blue",font="bold")
ent3.place(x=130,y=100)

btn1=Button(text="SAVE",foreground="white",background="blue",font="bold", command=save)
btn1.place(x=130,y=140)
btn2=Button(text="Delete",foreground="white",background="blue",font="bold",command=delete)
btn2.place(x=200,y=140)
btn3=Button(text="Search",foreground="white",background="blue",font="bold",command=search)
btn3.place(x=270,y=140)
btn3=Button(text="Edit",foreground="white",background="blue",font="bold",command=edit)
btn3.place(x=340,y=140)


window.mainloop()
