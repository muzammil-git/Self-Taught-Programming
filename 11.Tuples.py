#Concept: Immutable, You can't change the data inside Tuple when its created so choose carefullys.

#Creating Tuple 
my_tuple = ()
print(my_tuple)

#Storing
my_info = ("Muzammil", "22")
print(my_info)

#Iterating
for i in range(len(my_info)):
    print(my_info[i])

#Finding the value
print("22" in my_info)

if "Muzammil" in my_info:
    print("Yes its present")
else:
    print("Its not present")
