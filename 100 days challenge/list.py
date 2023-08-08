
marks = [1,4,6, "hassan", True]

print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

#Negative Indexing
print(marks[-4])

#changing it into positive indexing which is easy to identify in negative indexing
print(len(marks)-4)

print(marks[1])

if 6 in marks:
    print("Yes")
else:
    print("nO")