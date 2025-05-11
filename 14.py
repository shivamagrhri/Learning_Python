student = {
  "name" : "SHIVAM",
  "age" : 23,
  "subjects" : {
    "phy" : 97,
    "chem" : 98,
    "math" : 99
  }
}

# print(type(student))
# print(student.keys())
# print(list(student.keys()))
# print(len(student))

# print(student.values())
# print(student.items())
# print(student.get("name")) 
student.update({"city" : "Delhi"})
print(student)