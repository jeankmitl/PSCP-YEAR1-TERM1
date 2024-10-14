'''duplicate'''
def main():
    '''meow'''
    set_ax = int(input())
    set_bx = int(input())

    set_a = {}
    set_a = set(set_a)
    set_b = {}
    set_b = set(set_a)
    for _ in range(set_ax):
        num = int(input())
        set_a.add(num)
    for _ in range(set_bx):
        num = int(input())
        set_b.add(num)
    set_ab = set_a & set_b
    if set_ab == set({}):
        print('Nope')
    else:
        set_ab = reversed(sorted(set_ab))
        for i in set_ab:
            print(i)
main()
