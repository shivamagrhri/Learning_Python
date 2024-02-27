# ques 1

# f = open("practice.txt", "w")
# f.write("Hi everyone")
# f = open("practice.txt", "a")
# f.write("\nwe are learning File I/O")
# f.write("\nusing Java")
# f.write("\nI like programming in Java.")
# f.close()

# alternate ques 1

# with open("practice1.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O")
#     f.write("\nusing Java\nI like programming in Java.")

# f.close()

# ques2

# with open("practice1.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice1.txt", "w") as f:
#     data = f.write(new_data)

# Ques3
# def check_for_word():
#     word = "learning"
#     with open("practice1.txt", "r") as f:
#        data = f.read()
#        if(data.find(word) != -1):
#         print("FOUND")
#        else:
#         print("Not Found")

# check_for_word()

# Ques4
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice1.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data ):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()


# Ques 5
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if (int(val)%2 == 0):
            count += 1
print(count, "Evens are in list")