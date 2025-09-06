"""
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")
def is_even(n):
    return n % 2 == 0 
    
main()
"""


def main():
    dificult = input("dificult or casual? ").strip().title()
    if not (dificult == "Dificult" or dificult == "Casual"):
        print("invalid input")
        return
    player = input("multiplayer or single-player ").strip().title()
    if not (player == "Multiplayer" or player == "Single-player"):
        print("invalid input")
        return
    if dificult == "Dificult" and player == "Multiplayer":
        recomended("Call of Duty")
    elif dificult == "Dificult" and player == "Single-player":
        recomended("God of War")
    elif dificult == "Casual" and player == "Multiplayer":
        recomended("Fortnite")
    else:
        recomended("The Last of Us")    



def recomended(game):
    print(f"we recomended you to play {game}")
    return
    
main()

