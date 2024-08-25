import random
from art import logo, vs
from game_data import data
from replit import clear


def neat(list):
    """Puts it in a more printable method"""
    name = list["name"]
    description = list["description"]
    country = list["country"]
    return f"{name} is a  {description} and is from {country} ."


def checker(which, a, b):
    """checks whether a is greater than be if it is , has the user taken a? if yes then it"""
    """returns true if not it returns false. if b is greater than a it goes to ele and checks if the user chose b"""
    if a > b:
        return which == "a"
    else:
        return which == "b"


# getting the main stuff
score = 0
continues = True
b = random.choice(data)
print(logo)
while continues:
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print(f"Compare A : {neat(a)}")
    print(vs)
    print(f"Against B : {neat(b)}")
    which = input("Who has more followers?:'A'or'B' ").lower()
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]
    higher = checker(which, a_followers, b_followers)
    clear()
    print(logo)
    if higher:
        score += 1
        print(f" You're right! Current score is {score}")

    else:
        continues = False
        print(f"Sorry that's wrong. Final score is {score}")