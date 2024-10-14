'''phones CANT call!'''
def main():
    '''wmeow'''
    phone_num = input()
    phone_numlength = len(phone_num)
    region = input()
    if phone_numlength == 9:
        inter = f'+66 {phone_num[1:5]} {phone_num[5:]}'
        domest = f'0 {phone_num[1:5]} {phone_num[5:]}'
    else:
        inter = f'+66{phone_num[1]} {phone_num[2:6]} {phone_num[6:]}'
        domest = f'0{phone_num[1]} {phone_num[2:6]} {phone_num[6:]}'
    if region == 'International':
        print(inter)
    else:
        print(domest)
main()
