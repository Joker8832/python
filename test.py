name=["Anu","Manju","Vinod"]
select=int(input("Select A Option (1.Add 2.Select 3.Edit 4.Delete):"))
if select==1:
    n=(input("Enter A Name"))
    name.append(n)
    print(name)
elif select==2:
    n=(input("Enter A Selected Name"))
    data=name.index(n)
    print("Your Selected Name Is",name[data])
elif select==3:
    n=(input("Enter A Edting  Name"))
    k=(input("Enter A Replacing Name"))
    data=name.index(n)
    name[data]=k
    print(name)
elif select==4:
    n=(input("Enter A Selected Name"))
    data=name.index(n)
    del name[data]
else:
    print("Invalid Option  ")