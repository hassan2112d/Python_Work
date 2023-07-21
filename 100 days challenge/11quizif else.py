import time


b = int(time.strftime("%H"))
c = int(time.strftime("%M"))
d = int(time.strftime("%S"))

if(b>=6 and b<12):
    print("Good Morning")
    
elif(b>19 and b<6 ):
    print("Good Night")
elif(b>=13 and b<17):
    print("Good Evening")
else:
    print("Error Time")




