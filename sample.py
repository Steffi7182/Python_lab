class student:
  def __init__(self, name, rollno, marks):
    self.name = name
    self.rollno = rollno
    self.marks = marks
s1 = student("John", 36, 56)
print("name of student is:")
print(s1.name)
print("roll number of student is:")
print(s1.rollno)
print("marks obtained by student:")
print(s1.marks)

