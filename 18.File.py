import os

my_path = os.path.join("User","muzammil","my.txt")
print(my_path)

# FILE Techniques.

# r  -> Reading only
# w  -> Writing only
# w+ -> Read & Write


# Creating a file and writing
get_file = open("wishlist.txt","w")
get_file.write("Eat Biryani\nCheter peter pitty pocket")
get_file.close()

# Reading the file 
with open("wishlist.txt") as f:
    print(f.read())


my_list = list()

with open("wishlist.txt") as f:
    my_list.append(f.read())

print(my_list)


# WRITING & READING CSV FILE

import csv

my_path = os.path.join("/home","dualweilder","Desktop","Self Taught Programmer","st.csv")
# /home/dualweilder/Desktop/Self Taught Programmer/st.csv
#Note: THe path should start from / (slash)
print(type(my_path))

with open(my_path, "w") as my_csv:
    write = csv.writer(my_csv, delimiter=",")
    write.writerow(["one","two","three"])
    write.writerow(["four","five","six"])

with open(my_path, "r") as my_csv:
    read = csv.reader(my_csv, delimiter=",")

    for row in read:
        print(','.join(row))
<<<<<<< HEAD
=======


# Dont come
>>>>>>> a7886af5fa4ca2c006920a6a618c217bd655da20
