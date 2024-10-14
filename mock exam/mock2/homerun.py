'''homerun'''
field = float(input())
rangefield = float(input())
HOMERUNS = 0
NUMCOUNT = 0
def dist(x):
    '''AHHHHHHHHHHHHHHHHHHHHHH'''
    if rangefield > x:
        return 1
    return 0
while True:
    if NUMCOUNT == field:
        break
    NUMCOUNT += 1
    rangehit = float(input())
    HOMERUNS += dist(rangehit)
print(int(HOMERUNS))
