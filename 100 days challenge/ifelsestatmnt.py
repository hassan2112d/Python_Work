####Condition Operators

# < , > , <= , => , == , =!
### The space below if to print is called indentiation

a = 65

if(a>64):
    print("You are not so old")
else:
    print("You are old")

##Nested IF Statement

b = -2/5

if(b<0):
    print("Your Number is negative")
elif(b>0):
    if(b<=10):
        print("Your number is below 10")
    elif(b>=10 and b<=20):
        print("Your number is between 10 to 20")
    else:
        print("Your Number is big")
else:
    print("Your number is out of context")
