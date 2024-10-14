'''milk'''
def milker():
    '''dragon milk'''
    price = int(input())
    bottlecap_trade = int(input())
    extra_amount = int(input())
    money = int(input())
    bottles = money // price
    bottlecaps = bottles
    if not bottlecap_trade:
        print(bottles)
    else:
        while bottlecaps >= bottlecap_trade:
            additional_bottles = (bottlecaps // bottlecap_trade) * extra_amount
            bottles += additional_bottles
            bottlecaps = (bottlecaps % bottlecap_trade) + additional_bottles
        print(bottles)
milker()
