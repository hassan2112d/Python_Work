#Select and print Divisible Numbers

a=[1,3,5,6,7,9,27]
count=0
for i in range(len(a)):
    if(a[i]%3==0):
        print(a[i],"is divisible by 3")
    else:
      print (a[i],"not divisible by 3")    
    
      

