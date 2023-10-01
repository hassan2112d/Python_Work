
a = input("Enter the Number: ")

try:
    for i in range(1,11):
       print(f"{int(a)}x{i} = {int(a)*i}")
except :
    print('Invalid Input')

print("Hello table finished")