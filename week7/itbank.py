'''i hate bank'''
def deposit(dep, account):
    '''dep'''
    account += dep
    return account
def withdraw(withdrw, account):
    '''with'''
    account -= withdrw
    return account
def bank():
    '''bank'''
    account = float(input())
    cash = float(input())
    command = ''
    warning = 0
    while True:
        if warning >= 3:
            break
        command = input()
        if command == 'end':
            break
        action = command[0]
        amount = float(command[2:])
        if action == 'D':
            if cash >= amount:
                account = deposit(amount, account)
                cash -= amount
                warning = 0
            else:
                warning += 1
        elif action == 'W':
            if account >= amount:
                account = withdraw(amount, account)
                cash += amount
                warning = 0
            else:
                warning += 1
        else:
            warning += 1
    print(f"{account:.2f}")
    print(f"{cash:.2f}")
bank()
