'''lotto'''
def main():
    '''GAMBLING!!!'''
    winning_numfront = []
    winning_numback = []
    jackpot = input()
    winner_2 = input()
    total_money = 0
    for _ in range(2):
        winning_numfront.append(input())
    for _ in range(2):
        winning_numback.append(input())
    bought_ticket = input()
    if jackpot == '000000':
        if bought_ticket in ['000001', '999999']:
            total_money += 100000
    elif jackpot == '999999':
        if bought_ticket in ['999998', '000000']:
            total_money += 100000
    else:
        if int(bought_ticket) == int(jackpot) - 1 or int(bought_ticket) == int(jackpot) + 1:
            total_money += 100000
    if bought_ticket == jackpot:
        total_money += 6000000
    if winner_2 == bought_ticket[-2:]:
        total_money += 2000
    if bought_ticket[:3] in winning_numfront:
        total_money += 4000
    if bought_ticket[-3:] in winning_numback:
        total_money += 4000
    print(total_money)
main()
