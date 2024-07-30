import random

def roll_dice():
    return random.randint(1, 6)

def flip_coin():
    return random.choice(['head', 'tail'])

def main():
    players = []
    for i in range(2):
        players.append({
            'name': input(f"Enter Player {i+1}'s name: "),
            'score': 0
        })
    
    current_player = 0
    
    while players[0]['score'] < 100 and players[1]['score'] < 100:
        print(f"\nCurrent Scores - {players[0]['name']}: {players[0]['score']}, {players[1]['name']}: {players[1]['score']}")
        input(f"\n{players[current_player]['name']}, press Enter to roll the dice and flip the coin...")
        
        dice_roll = roll_dice()
        coin_flip = flip_coin()
        
        print(f"Dice roll: {dice_roll}")
        print(f"Coin flip: {coin_flip}")
        
        if (dice_roll % 2 != 0 and coin_flip == 'head'):
            multiplier = 5
        elif (dice_roll % 2 == 0 and coin_flip == 'head'):
            multiplier = 5
        else:
            multiplier = 1
        
        players[current_player]['score'] += dice_roll * multiplier
        
        if current_player == 0:
            current_player = 1
        else:
            current_player = 0
    
    winner = players[0] if players[0]['score'] >= 100 else players[1]
    print(f"\nCongratulations! {winner['name']} wins with a score of {winner['score']}!")

if __name__ == "__main__":
    main()
