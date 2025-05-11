tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter your number: "))
i = 0
for el in tup:
  if(el == x):
    print("number found at idx", i)
    break
  i += 1