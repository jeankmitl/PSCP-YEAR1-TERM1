'''balls'''
def baller():
    '''baller'''
    height: float = float(input())
    half: float = 0
    while height >= 0.01:
        height = height / 5 * 3
        half += 1
    print(half-1)
baller()
