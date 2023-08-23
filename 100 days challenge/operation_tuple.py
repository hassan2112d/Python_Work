# Tuple can only be changed when tuple is converted to list




a = (1,2,3,5,6,8,9,10,3,5,6,)

l = list(a)

l.append(2)
tup =tuple(l)
print(tup)



print(len(a))

b = a.count(3)
print(b)

c = a.index(3,5,12)

print(c)