#satchel lang
#10/17/2024
#procedures aka functions
#functions
def planet_name():
    print("---which planet are you?")
    print("answer these questions to find out!")
    ans = input("red (r), or blue (b):")
    if ans == "b":
       ans = input("flowers (f), or gemstones (g):")
       if ans == "f":
         ans = input("ocean (o), or mountain (m):")
         if ans == "o":
              print("congrats! your planet is earth")
         else:
              print("congrats! your planet is mercury")
    if ans == "g":
         ans = input("dawn (da), or dusk (du):")
         if ans == "da":
             print("congrats! your planet is uranus")
         else:
             print("congrats! your planet is neptune")

    if ans == "r":
       ans = input("dust (d), or gas (g):")
       if ans == "d":
         ans = input("hot (h), or cold (c):")
         if ans == "h":
                print("congrats! your planet is venus")
         else:
                print("congrats! your planet is mars")
    if ans == "g":
            ans = input("beauty (b), or strength (s):")
            if ans == "b":
                print("congrats! your planet is saturn")
            else:
               print("congrats! your planet is jupiter")
    ans = input("do you want to play again? ")
    if ans == "yes":
         planet_name()
    else:
        exit()

#main
planet_name()

