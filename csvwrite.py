
#___________________Writing(Old Data Will Be Removed)____________________
import csv 
with open('Write.csv','w') as csvf:
    fieldnames=['Name','Class','Rank']
    writer=csv.DictWriter(csvf,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Rank':'A','Class':'CS','Name':'Ajith'})
    writer.writerow({'Rank':'','Class':'CS','Name':'Adhin'})
    writer.writerow({'Rank':'C','Class':'CS','Name':'Rinshad'})
    print("Writing complete")  

