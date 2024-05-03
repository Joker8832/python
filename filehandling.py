#TO CREATE A FILE OR ADD A TEXT BY REPLACING
fl=open("filehandling.txt","w")
fl.write("Hello World Welcome to python")
#TO READ/PRINT
fl=open("filehandling.txt","r")
content=fl.read()
print(content)
fl.close()