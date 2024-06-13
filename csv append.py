import csv

with open('Write.csv','a') as csvf:
    fieldnames=['Name','Class','Rank']
    writer=csv.DictWriter(csvf,fieldnames=fieldnames, delimiter=',')
    writer.writeheader()  
    def add():        
        c=(input("Enter The Name Of The Student :"))
        b=(input("Enter The Class Of The Student    :"))
        a=(input("Enter The Rank Of The Student :")) 
        # writer.writeheader()       
        writer.writerow({'Name':c,'Class':b,'Rank':a},)   
        print("Added Succesfully")  
        yn=(input("Do You Want To Add More  (Y/N):"))
        if yn=="y" or yn=="Y":
            add()
        else:
            print("Exited Succefully")
            exit()
