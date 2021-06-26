
import random
from art import logo

# global scope
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Wrong choice!") 

def game():
    print(logo)
    # choosing a random number between 10 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}")


    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")

    # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer,turns)       
        if turns == 0:
            return
        elif guess != answer:
            print("Guess again!")


game()