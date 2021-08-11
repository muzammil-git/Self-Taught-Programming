# Concept: List is mutable means can be changed, list can store values of any type.

fruits = ["apple", "banana","Cherry"]
fruits[1] = "Orange"    #Replaces 1th index element
fruits.pop() #Removes the element at the n-1 index
fruits.append("Pear") #Adds Element
print(fruits)

exported_fruits = fruits
imported_fruits = ["KIWI", "Pumpkin","BlueBerry"]

print(f"Exported Fruits: {exported_fruits}")
print(f"Imported Fruits: {imported_fruits}")

#Concatenating List
print(f"All Fruits: {imported_fruits+exported_fruits}")


#Iterating fruits
for i in range(len(fruits)):
    print(fruits[i])

#Making exception just to test
try:
    print(fruits[1000])
except Exception:
    print("Something went wrong")


#List Guess Game

colors = ["Red", "Yellow", "Green"]
guess = input("Guess the color: ")

if guess in colors:
    print(f"You are right its {guess}")
else:
    print("You are wrong")