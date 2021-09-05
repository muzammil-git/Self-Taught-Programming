# STRING
name = "Syed"

for i in name:
    print(i) 

# LIST
game = ["NFS","Dune Buggy","FIFA","CS1.6","DBZ Mugen Edition"]

for i in game:
    print(i)  

# TUPLE
core_value = ("Integrity", "Resilience", "Can-do")

for i in core_value:
    print(i)

# Dictionary

name_age = {
    "Muzammil" : 22,
    "Ahsan" : 21
}

for i in name_age:
    print(i) #Prints key
    print(name_age[i]) #Prints value




game_list= ["NFS","Dune Buggy","FIFA","CS1.6","DBZ Mugen Edition"]
print(game_list)
counter=0

for i in game_list:
    game_list[counter] = i.upper()
    counter+=1

print(game_list)

#-----------------x---------------

game_listA = ["NFS","Dune Buggy","FIFA"]
game_listB = ["CS1.6","DBZ Mugen Edition","FAR CRY 4"]

all_games = []

for game in game_listA:
    all_games.append(game)

for game in game_listB:
    all_games.append(game)

print(all_games)    
