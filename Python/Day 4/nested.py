students = {
    "name" : "Shivam Agrahari",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

# print(students["subjects"]["chem"])
# print(students.keys())
# print(len(list(students.keys())))
# print(list(students.values()))
# print(students.items())
# print(students.get("name"))
students.update({"city":"Varanasi"})
print(students)