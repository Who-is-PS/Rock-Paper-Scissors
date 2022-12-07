import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
options_1 = ["✊🏻", "✋🏻", "✌🏻"]
while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options: 
        continue
    
    random_number = random.randint(0,2)
    # 0 = rock, 1 = paper, 2 = scissors
    computer_pick = options_1[random_number]
    print(f"Computer picked {computer_pick} .")

    if user_input == "rock" and computer_pick == "✌🏻":
        print("You won! ✊🏻 beats ✌🏻")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "✊🏻":
        print("You won! ✋🏻 beats ✊🏻")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "✋🏻":
        print("You won! ✌🏻 beats ✋🏻")
        user_wins += 1
    else:
        print(f"You lost! {computer_pick} beats {user_input}")
        computer_wins += 1    


print(f"You won {user_wins} times and the computer won {computer_wins} times.")
print("Goodbye!")
