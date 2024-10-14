'''validLmao'''
def symcheck(x):
    '''check special'''
    amount = len(x)
    result = True
    special = ['if', 'else', 'elif','while','for','True','False','continue','break', \
        'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']
    symbols = ['~', '!', '@', '`', '#', '$', '%', '^', '&', '*', "(", ')', '-', '=', '+' \
        '|', '[', ']', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?']
    for i in range(amount):
        if x[i] in symbols:
            result = False
    for j in range(1, amount-1):
        if x[j] in ' ':
            result = False
    if x[0].isnumeric():
        result = False
    if x in special:
        result = False
    if x[0] in ' ' and amount < 3:
        result = False
    return result
def checker():
    '''AAAAAAAAAAAAH'''
    names_amount = int(input())
    names_lis = []
    for _ in range(names_amount):
        names_lis.append(input())
    for k in names_lis:
        if symcheck(k) is False:
            print('Invalid')
        else:
            print('Valid')
checker()
