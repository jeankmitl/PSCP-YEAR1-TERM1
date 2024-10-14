'''ph'''
def main():
    '''aaa'''
    x = float(input())
    if x < 0 or x > 14:
        print('error')
    elif x < 7:
        print('acidic')
    elif x == 7:
        print('neutral')
    elif x <= 14:
        print('akaline')
main()
