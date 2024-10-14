'''restuarant'''
def rest():
    '''meow'''
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    if a >= b:
        meow = a - (a * c / 100)
    else:
        meow = a
    woof = (a + d) - ((a + d) * c / 100)
    if meow > woof:
        return f"Yes {meow-woof:.3f}"
    if woof > meow:
        return f"No {woof-meow:.3f}"
    return "Yes"
print(rest())
