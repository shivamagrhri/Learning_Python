# n = int(input("Enter the number"))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("total factorial =", fact)


n = int(input("Enter the number: "))

fact = 1
i = 1

while i<=n:
    fact *= i
    i += 1
print("total factorial =", fact)