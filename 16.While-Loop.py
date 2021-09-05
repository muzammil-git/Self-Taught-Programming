x = 8

while x > 0:
    print(x)
    x-=1

print("Happy New Year!")

#-----------------------x------------------------------

for i in range(1, 100):
    print(i)
    break;



n = 0

while True:
    if n == 10:
        break;

    print(n)
    n+=1;

# NESTED LOOP

for i in range(1,3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)



# Press n to quit

# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# added = []

# for i in list1:
#     for j in list2:
#         added.append(i+j)

# print(added)

# while input('y or n? ')!='n':
#     for i in range(1,6):
#         print(i)



print("-------------x------------------")

number = [5,1,9,10]
while True:
    x = input('Guess the number?: ');

    if x == "q":
        break;
 
    try:
        x = int(x)
    except ValueError:
        print('Write a number or \'q\' to quit')

    if x in number:
            print("Guessed Right!")
            break;
    else:
        print("Guessed Wrong!")
    
    for i in number:
        print(i)



print("---------------x--------------")

number = 10
while number >= 0:
    print(number)
    number -= 1



import keyword;
print(keyword.iskeyword("while"))