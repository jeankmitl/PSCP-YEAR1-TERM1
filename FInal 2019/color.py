"""Colors"""
def color(fir, sec):  #fir = first, sec = second cause lines are too long lol
    """colrof idner"""
    #these just mixes colors, if it isn;'t a valid color it'll output nuh uh
    if (fir == 'Red' and sec == 'Yellow') or (fir == 'Yellow' and sec == 'Red'):
        print('Orange')
        return

    if (fir == 'Red' and sec == 'Blue') or (fir == 'Blue' and sec == 'Red'):
        print('Violet')
        return

    if (fir == 'Yellow' and sec == 'Blue') or (fir == 'Blue' and sec == 'Yellow'):
        print('Green')
        return
    print('Error')

def summary(fir, sec):
    """this jsut covers everything else"""

    if not fir in('Red','Yellow','Blue') or not sec in('Red','Yellow','Blue'):
        print('Error')
        return

    if fir == sec:
        print(fir)
        return

def main():
    """aaaaaaa"""
    type_1 = input()
    type_2 = input()

    if type_1 == type_2:
        summary(type_1,type_2)
    else:
        color(type_1,type_2)
main()
