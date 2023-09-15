a = {
    1 : "hassan",
    2 : "shayan",
    3 : "mazahir",
    4 : "muslim",
    5 : "raza",
 }

print(a[4])

# print only keys of dictonaries
print(a.keys())

# print only values of dictonaries
print(a.values())

# get will not give error like ['']

print(a.get(5))

for b in a.keys():
    print(b)

for c,d in a.items():
    print("key is ",c,"value is:  ", d)