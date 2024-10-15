
'''pro'''
def main():
    '''pro'''
    pro_peep = int(input())     #people needed for promotion
    pro_pay = int(input())    #apay for only x people
    price = int(input())      #initial price
    people = int(input())     #people who came (pls)
    totalprice = 0

    totalprice += (people // pro_peep) * pro_pay
    totalprice += ((people - (people // pro_peep)) * price)

    print(price)
main()
