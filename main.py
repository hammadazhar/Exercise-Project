# In this program user give the file name and data to store!

total_title = 3

for i in range(total_title):

    fileName = input(f"{i+1} file name plz: ")
    text = input("Add data in file: ")
    total_title = fileName

    f = open(fileName+'.file', "w")
    f.write(text)
    f.close()

    f = open("all_file_name.txt", "a")
    f.write(fileName+",")
    f.close()

print("\nThe given content is written on the file successfully!")
