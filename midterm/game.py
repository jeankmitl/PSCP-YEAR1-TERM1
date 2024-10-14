'''game'''
def gamer():
    '''gameeee'''
    a= int(input())
    b = int(input())
    abruh = a%3
    bbruh = b%3
    if not a or not b:
        print(0)
    elif bbruh == abruh:
        print(bbruh)
    else:
        print('Error')
gamer()
