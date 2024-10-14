'''calc'''
meow = int(input())
def calc(x):
    """calc"""
    total = 0
    if x < 10:
        total = x * 2
    elif x >= 10:
        total = (9 * 2) + ((x - 9) * 3)
    elif x >= 100:
        total = (9 * 2) + (90 * 3) + ((x - 99) * 4)
    elif x >= 1000:
        total = (9 * 2) + (90 * 3) + (900 * 4) + ((x - 999) * 5)
    elif x >= 10000:
        total = (9 * 2) + (99 * 3) + (999 * 4) + ((x - 999) * 5)
    return total
print(calc(meow))
