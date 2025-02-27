import random

def dice_game():
    user_name = input("What is your name: ")
    
    user_score = 0
    computer_score = 0
    
    while user_score < 30 and computer_score < 30:
        print("####################")
        input("Press enter to roll the die " + user_name)
        
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        
        print(user_name + " rolled a " + str(user_roll))
        print("Computer rolled a " + str(computer_roll))
        
        if user_roll == 1:
            print("Oops " + user_name + " has to start over")
            user_score = 0
        else:
            user_score = user_score + user_roll
        
        if computer_roll == 1:
            print("Oops Computer has to start over")
            computer_score = 0
        else:
            computer_score = computer_score + computer_roll
        
        print(user_name + "'s Score: " + str(user_score))
        print("Computer's Score: " + str(computer_score))
    
    print("####################")
    
    if user_score >= 30:
        print(user_name + " Wins!")
    else:
        print("Computer Wins!")

dice_game()