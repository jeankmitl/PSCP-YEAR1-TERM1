'''elo'''
def aside(rx,ry):
    '''a'''
    meow = (ry - rx) / 400
    meow2 = 1 / (1 + (10**meow))
    return meow2
def bside(rx,ry):
    '''a'''
    meow = (rx - ry) / 400
    meow2 = 1 / (1 + (10**meow))
    return meow2
def main():
    '''elope'''
    ra = int(input())
    rb = int(input())
    choose = input()
    if choose == 'A':
        print(f'{aside(ra,rb):.2f}')
    else:
        print(f'{bside(ra,rb):.2f}')
main()
