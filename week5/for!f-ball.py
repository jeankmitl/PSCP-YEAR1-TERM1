'''BALLS'''
def positioner():
    '''BALL SQUEEZER'''
    randomizer = input()
    position = 1
    for i in randomizer:
        if position == 1:
            if i == 'A':
                position = 2
            elif i == 'C':
                position = 3
        elif position == 2:
            if i == 'A':
                position = 1
            elif i == 'B':
                position = 3
        else:
            if i == 'B':
                position = 2
            elif i == 'C':
                position = 1
    print(position)
positioner()
