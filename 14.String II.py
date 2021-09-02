
#STRINGS

print("She" in "She is working part time")

print("She" not in "She is working part time")

print("She said,\"I will leave early\".")

print('TODO task:\nPolish shoes\nMake breakfast\nSet goals')

#SLICING

name = ["Muzammil", "Ahsan", "Fouzan", "Sherry","Haseeb"]

print(name[0:3]) #start inclusive, end exclusive

quote = "\"Power comes in response to a need\""
print(quote[0:12]) #start inclusive, end exclusive
print(quote[13:]) #start inclusive, end exclusive

print(quote[:])

mom_said = "You are useless"
mom_said = mom_said.replace('useless', 'useful')

#USE CASE
email_address = "syedmuzammil@gmail.com"
email_address = email_address.replace('@','(at)')

print(mom_said)
print(email_address)


# Finding index of character in string
print("HEY".index('Y'))



my_string = "It was a bright cold day in April, and the clocks were striking thirteen."
my_string = my_string.split(',')

print(my_string[0])
