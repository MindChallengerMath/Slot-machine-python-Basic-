import random
items = ("Apple", "Orange", "Banana", "Posion", "Rot")
points = 0
def spin_row(options):
    result = (options[random.randint(0,4)],
              options[random.randint(0,4)],
               options[random.randint(0,4)] )
    return result
def print_row():
    slots = spin_row(items)
    return slots
def get_payout(player_roll):
    payout = 0
    if player_roll.count("Apple") > 1:
            payout += player_roll.count("Apple")
    elif player_roll.count("Orange") > 1:
            payout += player_roll.count("Orange")
    elif player_roll.count("Banana") > 1:
            payout += player_roll.count("Banana")
    else:
        print("You lose.")
    return payout
def player_bet(bet, balance):
    while True:
            bet = input("Enter dollars: ")
            try: 
                val = int(bet)
                if 0 < val <= balance:
                    return val
                else: 
                    print("Enter a valid number.")        
            except ValueError:
                print("Enter a valid answer.")
            
def main():
    global points
    balance = 1000
    while balance > 0:
        payday = 0
        print(balance)
        print("-------------------------")
        my_bet = player_bet(None, balance)
        balance -= my_bet
        spin = print_row()
        print("-------------------------")
        print(f"{spin[0]}:{spin[1]}:{spin[2]}")
        print("-------------------------")
        payday = get_payout(spin)
        balance += my_bet*payday
        points += 10*payday*my_bet
     



    

if __name__ == "__main__":
    main()
    print("-------------------------")
    print("Final Score")
    print("-------------------------")
    print(f"{points} points!") 