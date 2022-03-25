class Todo:

    def __init__(self, file_name, data,):
        self.file_name = file_name
        self.data = data

        f = open(file_name + ".txt", "a")
        f.write(data)
        f.close()


f1 = Todo(input("File name plz: "), input("Add data in the file: "))
f2 = Todo(input("2nd File name plz: "), input("Add data in the file: "))

x = int(input('Any file do you want to see type the name plz: '))

if x == 1:
    print(f1.__dict__)

elif x == 2:
    print(f2.__dict__)
