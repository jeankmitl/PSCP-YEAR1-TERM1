'''i hate my life and i want to die'''
def seller():
    '''cause i aint got no iphone'''
    model = input()
    size = input()
    baseprice = 0
    if model == 'iPhone 13 mini':
        baseprice += 25900
    elif model == 'iPhone 13 Pro Max':
        baseprice += 42900
    elif model == 'iPhone 13 Pro':
        baseprice += 38900
    elif model == 'iPhone 13':
        baseprice += 29900
    else:
        baseprice += -1000000
    if size == '128 GB':
        baseprice += 0
    elif size == '256 GB':
        baseprice += 4000
    elif size == '512 GB':
        baseprice += 12000
    elif model in ['iPhone 13 Pro', 'iPhone 13 Pro Max'] and size == '1 TB':
        baseprice += 20000
    else:
        baseprice += -1000000
    if baseprice < 0:
        print('Not Available')
    else:
        print(baseprice)
seller()
