
a = [12,45,65,67,75,34,45]

for b in a:
    print(b)
    if(b == 65):
        print("Hello!")

#In emurate you did  not have to identified the index in it  
#By default it takes the start= 0 but you can put like i did
#for index,c in enumerate(a):
for index,c in enumerate(a,start=1):
   
     print(f"index : {index} ,fruits : {c}")