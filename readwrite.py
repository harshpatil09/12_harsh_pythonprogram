File1=open("abc.txt","r+")
File1.write("Welcome to DYP")
File1.write("\nWelcome to CSE")
for i in File1:
 print(i)
File1.close()