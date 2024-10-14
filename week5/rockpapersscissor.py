'''rps'''
def game():
    '''rps'''
    game_result = input()
    a_wins = 0
    b_wins = 0
    for i in range (0, len(game_result), 2):
        if game_result[i:i+2] in ['PR', 'SP', 'RS']:
            a_wins += 1
        elif game_result[i:i+2] in ['RP', 'PS', 'SR']:
            b_wins += 1
    if not a_wins == b_wins:
        if a_wins > b_wins:
            print(f"A win {a_wins}-{b_wins}")
        elif b_wins > a_wins:
            print(f"B win {b_wins}-{a_wins}")
    else:
        print(f"DRAW {a_wins}")
game()
