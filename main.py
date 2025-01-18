import random
from art import logo
from art import vs
from game_data import data

def account_out (account):
    accout_name = account["name"]
    accout_description = account["description"]
    accout_country = account["country"]
    return f" {accout_name} , {accout_country} , {accout_description}"

def check_answer (user_input , a_follower , b_follower ):
    if a_follower > b_follower:
        return user_input == "A"
    else:
        return user_input == "B"


print(logo)
score = 0
game_on = True
account_b = random.choice(data)

while game_on:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Comapre A: {account_out(account_a)}")
    print(vs)
    print(f"Against B: {account_out(account_b)}")

    user_input = input("Who has more followers 'A' or 'B' : ").upper()

    print("\n" * 20)
    print(logo)

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(user_input , a_follower , b_follower)

    if is_correct:
        score +=1
        print(f"CORRECT current score {score}")
    else:
        print(f"Better Luck Next time!! , final score is {score}")
        game_on = False
