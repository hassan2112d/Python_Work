


a=int(input("Enter Maths Marks : \n "))
b=int(input("Enter Physics Marks : \n "))
c=int(input("Enter English Marks : \n "))
d=int(input("Enter Islamiat Marks : \n "))
e=int(input("Enter Urdu Marks : \n "))
total=int(input("Enter Total Marks : \n "))


abc=a+b+c+d+e

per=(abc/total)*100

if(per==50):
    print("You are just passed . Your Percentage is :",per)
    
elif(per<60): 
    print("Average Marks  . Your Percentage is : " , per)

elif(per<70):
    print("Good Marks  . Your Percentage is :  " , per)

elif(per<80):
    print("Very Good Marks  . Your Percentage is :" , per)

elif(per<90):
    print("Excellent MARKS  . Your Percentage is :" , per)

else:
    print("You are failed . Your Percentage is :" ,per)   

max=max(a,b,c,d,e)
min=min(a,b,c,d,e)

print("Your maximum marks is : \n " , max )
print("Your minimum marks is : \n " , min )



