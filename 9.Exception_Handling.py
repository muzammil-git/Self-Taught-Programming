
#To handle zero division error
"""
a = input('Enter First Number: ')
b = input('Enter Second Number: ')

try:
    sum = int(a)/int(b)
    print(sum)
except ZeroDivisionError:
    print("infinity")

"""



###Program for the wrong input and handling through exception###

#Case:
# Write a program that asks the user to type a number,
# convert it to an integer, and print it. 
# If you can't convert their input to an integer,
# print a message that says "Please type an integer."

user = input("Type a number: ")

try:
    print(int(user))
except Exception:
    print("Please type an integer.")