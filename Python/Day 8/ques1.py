class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_Avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your Average score is", sum/3)

s1 = Student("Shivam Agrahari", [99,99,98])
s1.get_Avg()

s1.name = "Satyam Agrahari"
s1.get_Avg()
