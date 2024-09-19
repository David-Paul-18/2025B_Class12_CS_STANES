#Program 6 - RANDOM GENERATOR (DICE GAME)

import random
print("\t\t\tDICE GAME")
print("\t\t\t*********")
moves=int(input("How many moves do you want to play? "))
for loop in range(moves):
    print("\nMove",loop+1)
    print("\tYour Turn")
    print("\t---------")
    key=input("Press any key to roll the dice (Press Enter to skip)... ")
    if key:
        print("You --> ",random.randint(1,6))
    else:
        print("Skipped...")
    print("\tComputer's Turn")
    print("\t---------------")
    print("Computer --> ",random.randint(1,6)) 
