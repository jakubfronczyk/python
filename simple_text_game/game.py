import random

class Game:
    def __init__(self):
        self.current_room = 1

    def start(self):
        print("Welcome to the game!")
        player_name = input("What's your name? ")
        print(f"Hello {player_name}! You find yourself in the rooms of riddels! To pass each room you have to complete the task in the room")
        self.play_room()

    def play_room(self):
        if self.current_room == 1:
            room1 = RiddleRoom("Riddle Room", "What has a head and a tail, but no body?", "coin")
            while room1.enter() == False:
                action = input("You can try again or quit the game (yes/no): ").lower()
                if action == "no":
                    print("Thanks for playing")
                    return
            print("Congratulations! You have passed the first room.")
            self.current_room += 1
        if self.current_room == 2:
            room2 = MathRoom("Math Room", "Using only addition, add eight 8's to get 1000.", "888+88+8+8+8")
            while room2.enter() == False:
                action = input("You can try again or quit the game (yes/no): ").lower()
                if action == "no":
                    print("Thanks for playing")
                    return
            print("Congratulations! You have passed the second room.")
            self.current_room += 1
        if self.current_room == 3:
            room3 = GuessingRoom()
            while room3.enter() == False:
                action = input("You can try again or quit the game (yes/no): ").lower()
                if action == "no":
                    print("Thanks for playing")
                    return
            print("Congratulations! You have passed the third room.")
            print("Thanks to that you win this game and now you can go free!")


class RiddleRoom:
    def __init__(self, name, riddle, answer):
        self.name = name
        self.riddle = riddle
        self.answer = answer
    
    def enter(self):
        print(f"You have entered the {self.name}.")
        print("To pass the room, you must guess the answer to this riddle.\n")
        print(self.riddle)
        player_guess = input("\nYour answer: ").lower()

        if player_guess == self.answer:
            return True
        else:
            print("Sorry, that is incorrect. Please try again.")
            return False

class MathRoom(RiddleRoom):
    def enter(self):
        while True:
            print(f"You have entered the {self.name}.\n")
            print(self.riddle)
            guess = input("\nEnter your answer(please don't use white spaces): ")
            if guess == self.answer:
                return True
            else:
                print("Incorrect answer. Try again.")

class GuessingRoom:
    def __init__(self):
        self.name = "Guessing Room"
        self.number = random.randint(1, 10)
        
    def enter(self):
        print(f"You have entered the {self.name}.\n")
        print("To pass the room, you must guess the number I'm thinking of (between 1 and 10).")
        attempts = 0
        while attempts < 3:
            guess = int(input("Your guess: "))
            if guess == self.number:
                return True
            elif guess < self.number:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
            attempts += 1
        print("Sorry, you have failed to guess the number in 3 attempts.")
        return False



game = Game()
game.start()
