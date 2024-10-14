'''longer'''
import math
def bwall():
    '''BALLS!!!!'''
    r = float(input())
    a = float(input())
    b = float(input())
    circlering =  2 * math.pi * r
    rectanglering = (a * 2) + (b * 2)
    if circlering > rectanglering:
        print('Circle is longer')
        print(f"{circlering-rectanglering:.5f}")
    elif rectanglering > circlering:
        print('Rectangle is longer')
        print(f"{rectanglering - circlering:.5f}")
    else:
        print('Equal')
        print("0.00000")
bwall()
