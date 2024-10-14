'''blackjack'''
def ace_checker(x):
    '''bruh'''
    if x > 17:
        x += 1
    else:
        x += 11
        if x > 21:
            x -= 10
    return x
def counter():
    '''wow'''
    amount_cards = int(input())
    total = 0
    ace_times = 0
    for _ in range(amount_cards):
        card = input()
        if card.upper() in ("J", "Q", "K", "JACK", "QUEEN", "KING"):
            total += 10
        elif card.upper() in ("A", "ACE"):
            total = ace_checker(total)
            ace_times += 1
        else:
            total += int(card)
    while total > 21:
        if not ace_times:
            break
        total -= 10
        ace_times -= 1
    print(total)
counter()
