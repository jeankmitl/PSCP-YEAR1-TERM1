'''pair'''
def main():
    '''what'''
    pairs = input()
    amount = 0
    output = ''
    missed = 0
    for i in pairs:
        amount += pairs.count(i)
        if amount % 2:
            output += i
            missed += 1
        pairs = pairs.replace(i,'')
        amount = 0
    if missed > 0:
        print(output)
    else:
        print('fully paired')
main()
