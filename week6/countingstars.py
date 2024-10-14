'''countingstars'''
def main():
    '''coutn THEM'''
    sky = input().rstrip()
    comet = "~*"
    comet_2 = '*~'
    shooting_star = '*/'
    constellation = '**'
    comets = 0
    shooting_stars = 0
    constellations = 0
    i= 0
    while i < len(sky) - 1:
        if sky[i:i+2] in comet or sky[i:i+2] in comet_2:
            comets += 1
            i += 2
        elif sky[i:i+2] in shooting_star:
            shooting_stars += 1
            i += 2
        elif sky[i:i+2] in constellation:
            constellations += 1
            i += 2
        else:
            i += 1
    if not constellations and not comets and not shooting_stars:
        print('Tonight is a quiet night.')
    else:
        print(f'constellation: {constellations}')
        print(f'comet: {comets}')
        print(f'shooting star: {shooting_stars}')
main()
