'''[asswprd]'''
from math import log2
from math import floor
def entrop():
    '''passwordssss'''
    password = input().replace(' ', '')
    total = 0
    special = [
        '~', '!', '@', '`', '#', '$', '%', '^', '&', '*', '(', ')',
        '-', '=', '+', '|', '[', ']', ';', ':', '"', "'", ',', '<',
        '.', '>', '/', '?', '\\', '{', '}', '_'
    ]
    if any((i.isupper()) for i in password) is True:
        total += 26
    if any((i.islower()) for i in password) is True:
        total += 26
    if any((i.isnumeric()) for i in password) is True:
        total += 10
    if any(i in special for i in password) is True:
        total += 32
    entropy = floor(log2(total**len(password)))
    print(entropy)
    if entropy < 28:
        print('Very Weak')
    elif 28 <= entropy <= 35:
        print('Weak')
    elif 36 <= entropy <= 59:
        print('Reasonable')
    elif 60 <= entropy <= 127:
        print('Strong')
    else:
        print('Very Strong')
entrop()
