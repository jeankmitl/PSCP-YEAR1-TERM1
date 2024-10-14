'''i hate this'''
onesandzeros = input()
odd = input()
def counter(x, y):
    """counts things"""
    onetotal = 0
    for num in x:
        if num == "1":
            onetotal += 1
    if y == "Even":
        if onetotal % 2 == 0:
            return "0"
        else:
            return "1"
    else:
        if onetotal % 2 == 0:
            return "1"
        else:
            return "0"
print(onesandzeros + counter(onesandzeros, odd))
len()