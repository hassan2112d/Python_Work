
a = [12,45,65,67,75,34,45]

for b in a:
    print(b)
    if(b == 65):
        print("Hello!")

#In emurate you did  not have to identified the index in it  
for index,c in enumerate(a):
    print(c)
    if(index == 75):
        print("Welcome!")