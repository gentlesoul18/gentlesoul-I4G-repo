import random as rd

def picked_type(choose):

    choice_option = {"R": "Rock", "P":"Paper", "S":"Scissors"}

    for i in choice_option:
        if i == choose:
            return (choice_option[i])

while True:

    option = ["R", "P", "S"]
    player = input("enter 'R' for Rock, 'P' for Paper and 'S' for Scissors:  ").upper()
    computer = rd.choice(option)

    print(f"Player ({picked_type(player)}) : CPU ({picked_type(computer)})")


    if player == computer: 
        print("Its a tie")

    elif player in option:
        if  player == 'R' and computer == 'S':
            print("PLayer wins")

        elif player == 'S' and computer == 'P':
            print("Player wins")

        elif player == 'P' and computer == 'R':
            print("Player wins")

        else:
            print("Computer wins")
            break

            
    else:
        print("invalid input! enter correct input")

