import random

def pc_random():
    lst=["r","p","s"]
    r= random.choice(lst)
    return r

def play(pc):
    options={
        "r": {
            "p": "La pc saco paper perdiste bro",
            "s": "La pc saco Scissors ganaste bro"
            },
        "p": {
            "r": "La pc saco Rock ganste bro",
            "s": "La pc saco Scissors perdiste bro"
            },
        "s":{
            "r": "La pc saco Rock perdiste bro",
            "p": "La pc saco Paper ganaste bro"
        }               
    }
    
    player = input("Que elegis Rock (r), Paper (p) o Scissors (s)?")
    
    if player == pc:
        return print("La pc saco lo mismo que vos empataron")
    else:
        return print(options[player][pc])
    
def main():
    play(pc_random())
    while input("Jugas otra broski? (Y/N)").upper() == "Y":
        play(pc_random())
        
if __name__ == "__main__":
    main()
    