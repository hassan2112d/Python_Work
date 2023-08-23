# KON BANEGA CORORPATI
z = "Welcome to KBC \n You Will be asked 3 questions And you will won 3 corers. Questions are below "
print(z)
a=int(input( "9+5 = \n"  ))

if a == 14:
    c =1
    print("Your answer is correct. You have won",c,"coror")
    b =int(input("10 + 9 = \n"))

    if b == 19:
        d=2
        print("Your second answer is also correct congratulations.You have won",d,"coroers")
        e = int(input ("8*9 = \n" ))

        if e == 72:
            
            print("Your third question is correct.You have won",c+d,"corers")
            print("You have won",c+d,"corores")
        else:
            print("Your answer is incorrect.You have won",d,"corores")
            
    else:
        print("Sorry your second answer is incorrect.You have won",c,"corores")    

else :
    print("Sorry You are failed")

