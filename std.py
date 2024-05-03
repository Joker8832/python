file=open("std.txt","a")
def add():
    name=input("Enter The Name:")
    address=input("Enter The Address:")
    num=input("Enter The Number:")
    file.write("Name:"+name+"\n""Address"+address+"\n""Number:"+num+"\n""__________________""\n")
    print(name,"Details Added Succesfully")
for a in range(2):
    add()