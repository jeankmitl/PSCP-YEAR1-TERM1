'''shower'''
def main():
    '''i am hydrophobvi'''
    months = int(input())
    bills = float(input())
    over = float(input())
    extra = float(input())
    lower_than = float(input())
    total = 0
    for _ in range(months):
        water = float(input())
        you_pay = 0
        if water > over :
            over_water = water-over
            you_pay += (over_water*extra)+(over*bills)
        elif water <= over:
            you_pay += water*bills
        if you_pay <= lower_than:
            total += 0
        elif you_pay > lower_than:
            total += you_pay
    print(f'{total:.2f}')
main()
