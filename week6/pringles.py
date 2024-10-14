'''pringles'''
def main():
    '''yummy'''
    can_top = input()
    can_mid = input()
    can_bottom = input()
    inches = int(input())
    final = ''
    chips = 0
    chips_left = 0
    for i in can_mid[:inches]:
        if i == ')':
            chips += 1
    for i in can_mid[inches:]:
        if i == ')':
            chips_left += 1
    if not chips_left:
        final += 'None.'
    else:
        final += 'There are still some left.'
    print(chips)
    print(final)
    print(can_top)
    print(f'{(' ' * inches) + can_mid[inches:]}') # fix this
    print(can_bottom)
main()
