'''liftred'''
def main():
    '''lift'''
    #check
    amount = int(input())
    weight_allow = float(input())
    adult = False
    overweight = False
    total_w = 0
    for _ in range(amount):
        age = int(input())
        weight = float(input())
        total_w += weight
        if age >= 12:
            adult = True
        if total_w > weight_allow:
            overweight = True
    if adult is True and overweight is False:
        print('Safe')
    elif not amount:
        print('Safe')
    else:
        print('Not Safe')
main()
###fix test casses pls thx
