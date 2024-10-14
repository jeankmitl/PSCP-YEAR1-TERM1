"""Amefuri DRY"""
HOUR = int(input())
WEATHER = str(input()).upper()
def weather_report():
    """AAAAAAAAAAAAAAA SO DRYYYYYYYY"""
    TIME = HOUR
    WET = 8
    for i in WEATHER:
        if WET >= 16 :
            WET = 16
        if TIME > 24 :
            TIME = 1
        if not WET:
            break
        if 6 <= TIME < 18 and i != 'H':
            WET += day(i)
        elif 0 <= TIME < 6 or 18 <= TIME <= 24 and i != 'H':
            WET += night(i)
        if i == 'H':
            print('Lost')
            break
        TIME += 1
    if WET <= 0 :
        print('Dry')
    elif 'H' not in WEATHER:
        print(f'Still Wet (Wet Level: {WET:.2f})')
def day(spell):
    """:3"""
    if spell == 'C':
        return -0.50
    if spell == 'N':
        return -1.00
    if spell == 'W':
        return -1.50
    if spell == 'R':
        return 2
    if spell == 'S':
        return 3
    return 0
def night(spell):
    """3;"""
    if spell == 'C':
        return -0.25
    if spell == 'N':
        return -0.50
    if spell == 'W':
        return -0.75
    if spell == 'R':
        return 2
    if spell == 'S':
        return 3
    return 0
weather_report()
