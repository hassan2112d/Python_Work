

#Finally is used to executed where the error occured or not but it will be the question that normal print also print this
#but when this comes to functions or databasse and file breakdown normal prints not worked but finally statement works.



def hello():
    try : 
        l = [1,2,3,5,8]
        a = int(input("Enter Your Value"))
        print(l[a])
        return 1
    except :
        print('Error')
        return 0 

    finally :
        print("I will executed always")

x = hello()

print(x)