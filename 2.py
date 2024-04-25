name=[]
def start():
    select=int(input("select a number 1.Add 2.Select 3.Edit 4.Delete 5.Exit"))
    if select==1:
        n=input("Enter A Num")
        name.append(n)
        print(name)
        start()
    elif select==2:
        n=input("Enter A Selected Name ")
        if n in name:
            print(n)
        else:
            name.append(n)
            print(name)
            data=name.index(n)
            print("your selected name",name[data])
            start()
    elif select==3:
        n=input("Enter A Name")
        m=input("Enter replacing name ")
        if n in name:
            print(n)
            data=name.index(n)
            name[data]=n
            print(name)
        else:
            print(n,"the name is not listed")
            start()
    elif select==4:
        n=input("Enter the deleting name")
        data=name.index(n)
        del name[data]
        print(name)
        start()
    else:
        exit()
start()