f = open("demo.txt", "r")
data = f.read()
# data = f.read(5)
data = f.readline()
print(data)
# print(type(data))
f.close()