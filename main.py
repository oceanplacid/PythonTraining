import random


print ("R - Rock\nP - Paper\nS - Scissors")
options = {"R":"Rock", "P":"Paper", "S":"Scissors"}


def game_play():
    counter = 0
    user_input = ""
    ai_choice = ""
    
    while True:
        ai_choice = random.choice(list(options))
        try:
            user_input = str(input("Make A Choice: "))
        except ValueError as e:
            print ("Invalid Input - ", e)
        if (user_input not in list(options)):
            print ("Invalid Input\nTry Again\n")
            
        if (user_input in list(options)):
            print ("PLayer ("+ options.get(user_input) + ") : CPU (" + options.get(ai_choice) + ")")
            if (user_input == ai_choice):
                print ("We Have A Tie\nTry Again\ln")
                counter = counter + 1
                continue
            if (counter == 3):
                break             
            if (user_input == "R"):
                if (ai_choice == "S"):
                    print ("Rock Beats Scissors: You Win!")
                if (ai_choice == "P"):
                    print ("Paper Beats Rock: CPU Wins!")
                    
            if (user_input == "S"):
                if (ai_choice == "R"):
                    print ("Rock Beats Scissors: CPU Wins!")
                if (ai_choice == "P"):
                    print ("Scissors Beats Paper: You Win!")             
            
            if (user_input == "P"):
                if (ai_choice == "S"):
                    print ("Scissors Beats Paper: CPU Wins!")
                if (ai_choice == "R"):
                    print ("Paper Beats Rock: You Win!")
            if counter >= 0:
                exit()          
            
        else:
            counter = counter + 1
            
            if counter == 3:
                print("Game Over!!!")
                break
    
    
game_play()