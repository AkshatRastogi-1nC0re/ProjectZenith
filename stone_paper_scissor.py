import random

def SPS(user_val):

    value = random.choice(["Stone", "Paper", "Scissor"])
    if user_val == value:
        return value, "Tie"
    elif user_val.lower() == "stone" and value == "Scissor":
        return value, "Win"
    elif user_val.lower() == "stone" and value == "Paper":
        return value, "Lose"
    elif user_val.lower() == "paper" and value == "Stone":
        return value, "Win"
    elif user_val.lower() == "paper" and value == "Scissor":
        return value, "Lose"
    elif user_val.lower() == "scissor" and value == "Stone":
        return value, "Lose"
    elif user_val.lower() == "scissor" and value == "Paper":
        return value, "Win"
    else:
        return "There was some problem with the algorithm", "Try again later"
