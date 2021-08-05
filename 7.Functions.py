#Calculate the age of person till next year

def my_age_next_year(x):
    """

    Returns x+1.
    :param x: int.
    :return: int sum of x+1.
    """

    return x+1

z = my_age_next_year(4)

if z==5:
    print(f'Hey there! I am {z} years old')

else:
    print(f'Hey there! something went wrong')



# 3 Required Parameter and 2 optional parameter
def opt(x,y,z,a=1,b=0):
    return x,y,z,a,b

print(opt(1,2,3,9))