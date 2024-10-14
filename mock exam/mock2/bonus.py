'''bonus'''
def bonuscalc(wage, years, months):
    '''calc'''
    if months >= 10:
        years += 1
        months = 0
    months = 0
    bonus = wage * years
    if bonus > wage * 20:
        bonus = wage * 20
    if bonus > 1000000:
        bonus = 1000000
    elif bonus < 5000:
        bonus = 5000
    print(int(bonus))
bonuscalc(int(input()), int(input()), int(input()))
