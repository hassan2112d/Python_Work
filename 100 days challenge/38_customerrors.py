
#Raise is ued for custom error means that some errors are already made by python but som eerrors are made by custom
#if i want to make a program so i should make a custom error for it it will not be provided by python.

# a = int(input("Enter The number between 5 to 9 \n"))

# if(a<5 or a>9):
#     raise ValueError("Enter Value between 5 to 9")
# else:
#     print("The value is within the range")

#Quiz question in CWH
b = input("Enter the word quit \n")

if( b=="quit"):
   print("The statement is correct")
else:
    raise ValueError("You hAVE TO entered quit ")