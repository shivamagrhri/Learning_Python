list = [1,4,9,16,25,36,49,64,81,100]
x = 36
i=0
for val in list:
    if(val==x):
        print("Number found at idx", i)
        break
    i += 1