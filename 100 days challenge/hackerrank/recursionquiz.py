# fibonacci

def fibonacci(n):
    if(n == 0 or n == 1 ):
        return 1
    elif(n == 2):
        return fibonacci(1)+fibonacci(0)
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))


