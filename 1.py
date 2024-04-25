address={"name1":"Anu","name2":"Raju","name3":"Vinod"}
select=int(input("Select A Option (1.Add 2.Select 3.Edit 4.Delete):"))
if select==1:
    n=(input("Enter A Name :"))
    address["name4"]=n 
    print(address)
elif select==2:
    n=input("Enter A The Selecting id :")
    print(address[n])
elif select==3:
    n=(input("Enter A Edting  Name Id"))
    k=(input("Enter A Replacing Name "))
    address["name"+n]=k
    print(address)
elif select==4:
    n=(input("Enter A Deleting  Name"))
    del address [n]
    print(address)
else:
    print("Invalid option")