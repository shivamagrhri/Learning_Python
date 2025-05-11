tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
n = int(input("Enter the number: "))
while i < len(tup):
  if(tup[i] == n):
    print("Found at idx", i)
  else:
    print("Finding.....")
  i += 1