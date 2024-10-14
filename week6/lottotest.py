"""lotto"""
def main():
    """GMAIGNGNGGGGNGNGNGN!!!!!!!!"""
    jackpot = input()
    last_2 = input()
    front3_1 = input()
    front3_2 = input()
    back3_1 = input()
    back3_2 = input()
    ticket = input()
    money = 0
    nearjackpot1 = ""
    nearjackpot2 = ""
    if jackpot == "000000":
        nearjackpot1 = "000001"
        nearjackpot2 = "999999"
    elif jackpot == "999999":
        nearjackpot1 = "999998"
        nearjackpot2 = "000000"
    else:
        nearjackpot1 = f'{(int(jackpot)-1):06d}'
        nearjackpot2 = f'{(int(jackpot)+1):06d}'
    if ticket == jackpot:
        money += 6000000
    if ticket in nearjackpot1 or ticket in nearjackpot2:
        money += 100000
    if ticket[-2:] == last_2:
        money += 2000
    if ticket[:3] == front3_1:
        money += 4000
    if ticket[:3] == front3_2:
        money += 4000
    if ticket[-3:] == back3_1:
        money += 4000
    if ticket[-3:] == back3_2:
        money += 4000
    print(money)
main()
