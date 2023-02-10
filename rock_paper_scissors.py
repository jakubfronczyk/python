import random

while True:
        user_choice = input ("Enter a choice (rock, paper, scissorsr):")

        choices = ["rock", "paper", "scissors"]

        # function that returns a random element from a list
        computer_choice = random.choice(choices) 

        print (f"\nYour choice is **{user_choice}** vs Computer choice is **{computer_choice}**\n")

        if user_choice == computer_choice:
                print ("It is a draw !")
        elif user_choice == "rock" and computer_choice == "paper":
                print ("You lose. Paper covers Rock")
        elif user_choice == "paper" and computer_choice == "scissors":
                print ("You lose. Scissors cuts paper")
        elif user_choice == "scissors" and computer_choice == "rock":
                print ("You lose. Rock crushes scissors") 
        elif user_choice == "paper" and computer_choice == "rock":
                print ("You win. Paper covers Rock")
        elif user_choice == "scissors" and computer_choice == "paper":
                print ("You win. Scissors cuts paper")
        elif user_choice == "rock" and computer_choice == "scissors":
                print ("You win. Rock crushes scissors")

        play_again = input("Do you want to play again ? (yes/no): ")
        if play_again == "no":
                break