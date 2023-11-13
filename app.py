#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Make a rock, paper, scissors console game

def get_user_input():
    user_input = input("Enter rock, paper, or scissors: ")
    return user_input

def get_computer_input():
    import random
    computer_input = random.choice(["rock", "paper", "scissors"])
    return computer_input

def gameplay(user_input, computer_input):
    if user_input == computer_input:
        print("It's a tie!")
    elif user_input == "rock":
        if computer_input == "paper":
            print("You lose!")
        else:
            print("You win!")
    elif user_input == "paper":
        if computer_input == "scissors":
            print("You lose!")
        else:
            print("You win!")
    elif user_input == "scissors":
        if computer_input == "rock":
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
    print("Your choice: " + user_input)
    print("Computer's choice: " + computer_input)


def main():
    user_input = get_user_input()
    computer_input = get_computer_input()
    gameplay(user_input, computer_input)
    

if __name__ == "__main__":
    main()