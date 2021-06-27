from math import acos, e
from art import logo, vs 
from game_data import data
import os
import random


def format_data(account):
    """### Takes the account data and return the portable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}" 


def check_aswer(guess, a_followers, b_followers):
    """### Use if statement to check if user is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    

    # Making account at positionn B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}. ")
    print(vs)
    print(f"Compare B: {format_data(account_b)}. ")


    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_aswer(guess, a_follower_count, b_follower_count)
    # Clear The screen
    os.system('cls')
    # Dispalay art
    print(logo)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"Hurrey, Your'r right! Current score: {score} ")
    else:
        game_should_continue = False
        print(f"Sorry!, that's wrong. Final score: {score}.")




