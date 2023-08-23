import time


b = int(time.strftime(input("Enter your Hours Time:\n")))


print(b)

if(b>=6 and b<12):
    print("Good Morning")
    
elif(b>19 and b<6 ):
    print("Good Night")
elif(b>=13 and b<17):
    print("Good Evening")
else:
    print("Error Time")




