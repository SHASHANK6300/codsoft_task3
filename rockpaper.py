import random


user_score = 0
computer_score = 0


choices = ['rock', 'paper', 'scissors']

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

print("Welcome to Rock, Paper, Scissors!")

while True:
    
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

  
    result = determine_winner(user_choice, computer_choice)

    
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

   
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

   
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break
