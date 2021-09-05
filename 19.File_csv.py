
import csv;

data = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("/home/dualweilder/Desktop/Self Taught Programmer/movies.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    
    for row in data:
        writer.writerow(row)

    
with open("/home/dualweilder/Desktop/Self Taught Programmer/movies.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")

    for row in reader:
        # print(row)
        print(','.join(row))

<<<<<<< HEAD
=======
#HEy #Again Merged

#Test my file
>>>>>>> a7886af5fa4ca2c006920a6a618c217bd655da20
