def average(a,b):
    print("the average of" , (a+b)/2)

average(9,8)

# defautlt arguments

def average2(a=1,b=2):
    print("Average of a and b is ",(a+b)/2)


average2()

# Required Arguments 

def average3(a,b):
    return ((a + b )/ 2)

average3(4,5)