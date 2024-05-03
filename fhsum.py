n=int(input("Enter The First Number:"))
m=int(input("Enter The Second Number:"))
file=open("fhsum.txt","w")
sum=n+m
sub=n-m
mult=n*m
div=n//m
file.write("Sum:"+str(sum)+"\n""Substraction:"+str(sub)+"\n""Multilplication:"+str(mult)+"\n""Division:"+str(div)+"\n""---------------")
print("Succes")