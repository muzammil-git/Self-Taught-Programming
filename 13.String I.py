# ITERATING STRING 

animal_name = "Husky"

#Prints First index
print(animal_name[0])
#Prints last index
print(animal_name[-1])

#slicing reverse string #Least Running time as compared to For loop
s1 = animal_name[::-1] #start: stop: step
print(s1)

#Looping reverse string
for i in range(len(animal_name)-1,-1,-1):
    print(animal_name[i])

# Trying Exception #IndexError
try:
    print(animal_name[34])
except IndexError:
    print('Index not found')

#String Concatenation
first_name = "Syed Muzammil"
last_name = "Ali"

print(first_name+last_name)

#String Interpolation
name = "Muzammil"
age = 22

print(f"My name is {name} and I am {age} years old.")

#Prints 10 times
print("Hey"*10)


# Built in Method
print(name.upper())
print(name.lower())

print("----------------x--------------")


# Algorithm:
# Traverse the given string character by character upto its length, check if character is in lowercase or uppercase using built in methods.
# If lowercase, increment its respective counter, convert it to uppercase using upper() function and add it to a new string, if uppercase, increment its respective counter, convert it to lowercase using lower() function and add it to the new string.
# If space, increment its respective counter and add it to a new string
# Print the new string.


sent =  "I live in Pakistan and capital of Pakistan is Islamabad."

print(len(sent))

track_upperCase = 0
track_lowerCase = 0
track_space = 0

newString = ""

for letter in range(len(sent)):

    if(sent[letter].isupper()):
        track_upperCase +=1
        newString += sent[letter].lower()

    if(sent[letter].islower()):
        track_lowerCase +=1
        newString += sent[letter].upper()

    if(sent[letter].isspace()):
        track_space +=1
        newString += sent[letter]


    print(sent[letter],end ="")

print("\n")
print("---New String---")
print(f"Upper Case: {track_upperCase}")
print(f"Lower Case: {track_lowerCase}")

print(f"New String: {newString}")



# --------------------x--------------------

intro = "I am self motivated developer. who makes new ideas"

print(intro.split("."))


seperate_my_name  = "Muzammil"
print("-".join(seperate_my_name))

words = ["The", ""]

print(words)

a = "   Hello"
print(a)
a = a.strip()   
print(a)


senti = "aldous was born in 1894."
newString = ""

for i in range(len(senti)):
    if (i==0):
        newString+=senti[i].upper();
        continue;

    newString+=senti[i]
    
print(newString)

#-----------------------x-------------#

hey_input = "Where now? Who now? When now?"

new_hey_input= hey_input.split('?')

print(new_hey_input)

