def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n

cal = sum(5)
print(cal)
