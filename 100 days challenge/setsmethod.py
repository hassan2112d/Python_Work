
a = {2,6,7,8,9}

b ={1,3,4,5,6,10}

print(a.union(b))


# //Union do this AUB in actuall maths

#Update makes the a and b collaib it 

a.update(b)

print(a)

#intersection means in AnB in actuall maths
#intersection update will update c sets which are similar to both variables

c = {2,6,7,8,9}

d ={1,3,4,5,6,10}

e =c.intersection(d)

c.intersection_update(d)
print(c)

# Symetric difference and updates
# symetric difference are which are not common in both the sets and same processor for update as well which is mention above

f = {3,6,7,8,9}
g ={1,3,4,5,6,10}

print(f.symmetric_difference(g))

#difference and difference updates 
#difference is equal to A-B in atuall maths means that which are not common in first variables are to beconsidered and same goes for anotherevariable
#same goes for updates but which is mention in above 

print(f.difference(g))

#if there is no common thing in sets now we will used isdisjoint() built in function.Note: Answer will be in boolean 
x = {3,6,7,8,9}
y ={1,4,5,6,10}

print(x.isdisjoint(y))

#add()

x.add(10)
print(x)

#update() . if you want to add more item then one you will use update which is also be done above

#remove and discard(). difference between them is remove did not run furthere program if there is error in program
# and discard will run program if there is any mistake wil be seee in it.

y.remove(4)
x.discard(6)
print(y)
print(x)

#pop method takeout randomly one item from the given sets pop()

#del means delete the entire sets

#clear means clean the entire sets values

#condition in if we will use (in):
m ={1,4,5,6,10}


if 3 in m:
    print("yes")
else:
    print("No")