import csv
with open('DATA.csv',newline='') as csv_file: #data.csv=file name  
    csv_read=csv.reader(csv_file, delimiter=',') #delimiter=edhu mudhala skip akande aryan

    for a in csv_read:
        print(a[0]+" "+a[1])
