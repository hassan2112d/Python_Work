# the if and else condition in short hand is used for short scripts or for only short code and
# big conditions are used for big scripts

a = int(input("Enter Your First Number: \n"))
b = int(input("Enter Your Second Number: \n"))

#CompleX Conditions
print("A is bigger than B") if a>b else print("a and be both are same") if a==b else print("B is bigger than A")

#One line condition
c = 9 if a>b else 0

print(c)