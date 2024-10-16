'''atm'''
def main():
    """withdraw dem money"""
    money = int(input())
    stats = ''

    while True:
        stats = str(input())
        if stats == 'END':
            print(money)
            break

        process = stats.split(' ')

        if process[0] == 'D':
            money += int(process[1])

        if process[0] == 'W':
            moneyer = int(process[1])
            if moneyer > money:
                money = 0
            else:
                money -= moneyer
main()
