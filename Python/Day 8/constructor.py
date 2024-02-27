class Student :
    def __init__(self, name, marks) :
     self.name = name
     self.marks = marks
     print("Adding new student in the Database...")

s1 = Student("Shivam",98)
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)