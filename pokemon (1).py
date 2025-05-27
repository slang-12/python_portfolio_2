#satchel lang
#11/21/24
import random

pokemon_level = 0
pokemon_name = "charmander"
day = 0
wins = 0
losses = 0
evolution = False
evolution_2 = False

def train():
    print("your pokemon went to the gym to workout, +1 level!")
    global pokemon_level
    pokemon_level = pokemon_level + 1

def gym_battle():
    print("your pokemon is about to fight another pokemon in a gym battle! lets see if they can win -->")
    battle = random.randint(0,1)
    if battle == 1:
        print("congrats! your pokemon won the battle! +2 levels")
        global pokemon_level
        global wins
        pokemon_level = pokemon_level + 2
        wins = wins + 1
    else:
        print("oops, your pokemon lost the battle! -2 levels")
        global losses
        pokemon_level = pokemon_level - 2
        losses = losses + 1

def rest():
    print("your pokemon is taking a rest, lets check its stats: ")
    print ("level =" + str(pokemon_level))
    print ("name = " + pokemon_name)
    print ("wins =" + str(wins))
    print ("losses =" + str(losses))

def quit():
    print("buh bye :(")

def evolve():
    global pokemon_level
    global pokemon_name
    global evolution
    if pokemon_level > 9 and evolution == False:
        pokemon_name = "charmeleon"
        print("congrats! your charmander just evolved into a charmeleon!")
        evolution = True
    if pokemon_level > 19 and evolution_2 == False:
        pokemon_name > "charizard"
        print("congrats! your charmeleon just evolved into a charizard!")
        evolution = True

def pokemon_game():
    global day
    day = day + 1
    print("choose the activity for day " + str(day) + ": ")
    print("""1. Train
    2. Gym Battle
    3. Rest (Display Info)
    4. Quit""")
    option = input("(1-4) select an option: ")
    if option == "1":
        train()
        evolve()
        print(" ")
    if option == "2":
        gym_battle()
        evolve()
        print(" ")
    if option == "3":
        rest()
        print(" ")
    next = input("do you want to continue to the next day? (y) yes or (n) no: ")
    if next == "y":
        pokemon_game()
    else:
        exit()

def complete_poke_game():
    print("welcome to pokemon evolution! your pokemon is a charmander")
    pokemon_game()

#main
complete_poke_game()
