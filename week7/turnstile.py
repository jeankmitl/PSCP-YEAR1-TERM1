'''turnstile'''
def loop(x):
    '''loooooop THIS SHIT STAYS LOCKED!!!!!!'''
    turnstiler = 'locked'
    turns = 0
    for i in x:
        if turnstiler == 'locked':
            if i == 'C':
                turnstiler = 'unlocked'
        elif turnstiler == 'unlocked':
            if i == 'P':
                turns += 1
                turnstiler = 'locked'
    print(turns)
def main():
    '''mainminiinibyuidfgvyujiasdffvyusdwe'''
    i = True
    meow = []
    while i is True:
        x = input()
        if x == 'END':
            break
        meow.append(x)
    loop(meow)
main()
