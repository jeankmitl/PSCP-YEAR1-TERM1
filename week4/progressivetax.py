'''progtax'''
def theIRS(money):
    '''AAAAAAAHHHH TAXES!!!'''
    if money <= 150000:
        return 0
    elif money <= 300000:
        return money * (0.05)
    elif money <= 500000:
        return money * (0.10)
    elif money <= 750000:
        return money * (0.15)
    elif money <= 1000000:
        return money * (0.20)
    elif money <= 2000000:
        return money * (0.25)
    elif money <= 4000000:
        return money * (0.30)
    else:
        return money * (0.00)
print(theIRS(int(input())))