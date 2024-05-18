from tkinter import*
window=Tk()
window.title("Welcome to Apps")
window.geometry("250x250")
window.resizable(False,False)
window.configure(background="#14A3C7")
window.iconbitmap("favicon-32x32.png")
#window.attributes("-alpha",0.9)
window.attributes("-topmost",True)
def clicked(num):
    first_num=b1.get()
    b1.delete(0,END)
    b1.insert(0,str(first_num)+str(num))
def add():
    first_number=b1.get()
    global old_value
    old_value=int(first_number)
    global math 
    math="add"
    b1.delete(0,END)
def sub():
    first_number=b1.get()
    global old_value
    old_value=int(first_number)
    global math 
    math="sub"
    b1.delete(0,END)
def mult():
    first_number=b1.get()
    global old_value
    old_value=int(first_number)
    global math 
    math="mult"
    b1.delete(0,END)
def div():
    first_number=b1.get()
    global old_value
    old_value=int(first_number)
    global math 
    math="div"
    b1.delete(0,END)
def clear():
    b1.delete(0,END)
    b1.delete(END,0)

def equal():
    if math=="div":
        new_value=b1.get()
        b1.delete(0,END)
        b1.insert(0,int(old_value)/int(new_value))
    if math=="mult":
        new_value=b1.get()
        b1.delete(0,END)
        b1.insert(0,int(old_value)*int(new_value))
    if math=="add":
        new_value=b1.get()
        b1.delete(0,END)
        b1.insert(0,int(old_value)+int(new_value))
    if math=="sub":
        new_value=b1.get()
        b1.delete(0,END)
        b1.insert(0,int(old_value)-int(new_value))





    
    

b1=Entry(background="white",width=31)
b1.place(x=40,y=20)
btn1=Button(text="1",background="white",fg="black",height=1,width=3,command=lambda:clicked(1))
btn1.place(x=40,y=70)
btn2=Button(text="2",background="white",fg="black",height=1,width=3,command=lambda:clicked(2))
btn2.place(x=80,y=70)
btn3=Button(text="3",background="white",fg="black",height=1,width=3,command=lambda:clicked(3))
btn3.place(x=120,y=70)
btn4=Button(text="4",background="white",fg="black",height=1,width=3,command=lambda:clicked(4))
btn4.place(x=40,y=110)
btn5=Button(text="5",background="white",fg="black",height=1,width=3,command=lambda:clicked(5))
btn5.place(x=80,y=110)
btn6=Button(text="6",background="white",fg="black",height=1,width=3,command=lambda:clicked(6))
btn6.place(x=120,y=110)
btn7=Button(text="7",background="white",fg="black",height=1,width=3,command=lambda:clicked(7))
btn7.place(x=40,y=150)
btn8=Button(text="8",background="white",fg="black",height=1,width=3,command=lambda:clicked(8))
btn8.place(x=80,y=150)
btn9=Button(text="9",background="white",fg="black",height=1,width=3,command=lambda:clicked(9))
btn9.place(x=120,y=150)
btn0=Button(text="0",background="white",fg="black",height=1,width=3,command=lambda:clicked(0))
btn0.place(x=40,y=190)

btnsum=Button(text="+",background="white",fg="black",height=1,width=3, command=add)
btnsum.place(x=160,y=70)
btnsum=Button(text="-",background="white",fg="black",height=1,width=3, command=sub)
btnsum.place(x=160,y=110)
btnsum=Button(text="x",background="white",fg="black",height=1,width=3, command=mult)
btnsum.place(x=160,y=150)
btnsum=Button(text="/",background="white",fg="black",height=1,width=3, command=div)
btnsum.place(x=160,y=190)
btnsum=Button(text="=",background="white",fg="black",height=1,width=9, command=equal)
btnsum.place(x=80,y=190)
btnsum=Button(text="Clear",background="white",fg="black",height=9,width=3, command=clear)
btnsum.place(x=200,y=70)
window.mainloop()
