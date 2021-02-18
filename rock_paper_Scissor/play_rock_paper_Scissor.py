import random


# Create a list of play option

options=['Rock','Paper','Scissors']

computer=options[random.randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!",computer,"covers",player)
        else:
            print("You Won!!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!",computer,"covers",player)
        else:
            print("You Won!!", player, "smashes", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!",computer,"covers",player)
        else:
            print("You Won!!", player, "cut", computer)        
    else:
        print("That is not a valid move")
    player = False
    computer = options[random.randint(0,2)]