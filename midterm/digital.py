"""Digital"""
def main():
    """AAAAAAAAAAAAAHHHHHHHHHHH"""
    name = input()
    thai = input()
    house = input()
    age = float(input())
    wage = float(input())
    savings = float(input())
    con1 = False
    if thai in ['Yes', 'True'] and house in ['Yes', 'True']:
        con1 = True
    con2 = False
    if age >= 16:
        if savings <= 500000:
            if wage <= 840000:
                con2 = True
    bruh = ''
    if con1 is True and con2 is True:
        bruh = 'of 10,000 baht, sponsored by all taxpayers in Thailand.'
        print(f'Congratulations! {name} is qualified to receive a digital wallet amount ' + bruh)
    else:
        print(f'Unfortunately, {name} is not qualified.')
main()
