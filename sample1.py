class Student:
    def studentDetails(self):
        self.name=input("Enter name of student : ")
        self.rollno = input("Enter roll number: ")
        self.digital=int(input("Enter digital Marks : "))
        self.python= int(input("Enter python Marks : "))

    def Result(self):
        self.per= int( (self.digital + self.python) / 300 * 100 );
        print(self.name,self.rollno, self.per)

S1=Student()
S1.studentDetails()
print("Student details are:")
S1.Result()


