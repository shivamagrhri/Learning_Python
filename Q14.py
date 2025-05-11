marks = {}
x = int(input("Enter physics marks: "))
marks.update({"phy" : x})
y = int(input("Enter chemistry marks: "))
marks.update({"chem" : y})
z = int(input("Enter math marks: "))
marks.update({"math" : z})

print(marks)