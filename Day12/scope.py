# ----------------------SCOPE-------------------------

""" A variable is only available from inside the region it is created. This is called scope."""

# Local scope:

def game():
    player_health = 2
    print(player_health)

game()

# Global scope:

player_health = 10

def player():
    player_health = 3
    print(player_health)

player()
print(player_health)