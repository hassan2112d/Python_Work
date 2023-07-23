
a =int(input("Enter your Number : \n"))

match a :
    case 0:
        print("The value is zero")
    case 4 :
        print("The value is 4")
    case 9 :
        print("The value of a is 9")
    case _ if a!=90:
        print("the value of a is not 90")
    case _ :
        print("The value is out of context")