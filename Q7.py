a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if(a>b and a>c):
  print(a, " is the greatest number")
elif(b>a and b>c):
  print(b, " is the greatest number")
else:
  print(c, " is the greatest number")