class student:
    def __init__(self):
        self.name=[]

    def addStudent(self,Name):
        self.name.append(Name)
    
    def showStudent(self):
        for data in self.name:
            print(data)
    
    def searchStudent(self,Name):
        self.flag=0
        for data in self.name:
            if Name == data:
                print(Name,"is a student of class A")
                self.flag=1
                break
        if self.flag == 0:
            print(Name,"is not a student of class A")

    def removeStudent(self,Name):
        if Name in self.name:
            self.name.remove(Name)
            print(Name,"Removed")
        else:
            print(Name,"not in the list")

#main code
obj=student()

checker=1
print("OPTIONS \n1.Add student\n2.show student\n3.search student\n4.remove studnet\n0.for exit")
while checker !=0:
    checker=int(input("\nEnter the option:"))
    match checker:
        case 1:
            n=int(input("how many students to add:"))
            print("Enter the names")
            for i in range(n):
                name=input()
                obj.addStudent(name)

        case 2:
            print("\nstudent list")
            obj.showStudent()

        case 3:
            search=input("Enter the name to search:")
            obj.searchStudent(search)

        case 4:
            n=int(input("how many students to remove:"))
            print("Enter the names")
            for i in range(n):
                name=input()
                obj.removeStudent(name)

        case 0:
            print("Exiting")
            
        case _:
            print("invalid option...!")
