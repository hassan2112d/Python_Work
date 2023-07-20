a = "Harry!!!!!!!!!!!! Harry ali"

print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","hassan"))
print(a.capitalize())
# spilts make output in list or array form
print(a.split())

###Give space before it but it includes the length also of the variable

print(a.center(38))

print(a.count("Harry"))

##End with do that that some thing is ending accourding to you and it will answer in boolean form.

b = "Hassan is a good boy."

print(b.endswith("."))

###if no come after this it will figure out it is ending accourding to index 

print(b.endswith("a",5,11))

#simple findout

print(b.find("is"))

##Index error will give error if it is not found 

print(b.index("is"))