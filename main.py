# In this program user give the file name and data to store!

fileName1 = input("1st file name plz: ")
text = input("Add data in file: ")
f = open(fileName1+'.file', "w")
f.write(text)
f.close()

f = open("all file name.txt", 'a')
f.write(fileName1)
f.close()

fileName2 = input("2nd file name plz: ")
text = input("Add data in file: ")
f = open(fileName2+'.file', "w")
f.write(text)
f.close()

f = open("all file name.txt", 'a')
f.write("\n"+fileName2)
f.close()

fileName3 = input("3rd file name plz: ")
text = input("Add data in file: ")
f = open(fileName3+'.file', "w")
f.write(text)
f.close()

f = open("all file name.txt", 'a')
f.write("\n"+fileName3)
f.close()

print("\nThe given content is written on the file successfully!")
