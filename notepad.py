from tkinter import*
from tkinter import filedialog as fd
import tkinter.messagebox as Message

window=Tk()


window.title("Notepad")
window.geometry("500x500")
window.iconbitmap("favicon.ico")
window.resizable(True,True)
text=Text(wrap="word")
text.pack(side="top",fill="both",expand=True)

def new_file():
    text.delete("1.0","end")
    window.title("Notepad")
def open():
    file=fd.askopenfile(parent=window,mode="rb",title="Open A File")#rb=read binary
    if file:
        content=file.read()
        text.delete("1.0","end")
        text.insert("1.0",content)#0 or 1.0 is okay
        file.close()
        window.title(file.name)
def save():
    file=fd.asksaveasfile(mode="w",defaultextension=".txt",filetypes=[("Text Document","*.txt"),("All Files","*.*")])
    if file:
        content=text.get("1.0","end")
        file.write(content)
        file.close()
        window.title(file.name)
def cut():
    text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")


menubar=Menu()
window.config(menu=menubar)

file_menu=Menu(menubar)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open)
file_menu.add_command(label="Save",command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)
edit_menu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)
